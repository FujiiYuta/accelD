//
//  InterfaceController.swift
//  accelD WatchKit Extension
//
//  Created by 藤井悠太 on 2018/10/26.
//  Copyright © 2018年 100kw. All rights reserved.
//

import WatchKit
import Foundation
//新たに二つのライブラリをインポート
import WatchConnectivity
import CoreMotion
import HealthKit
import UserNotifications

//  機械学習用ライブラリ
import CoreML

class InterfaceController: WKInterfaceController, HKWorkoutSessionDelegate, WCSessionDelegate{
    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        
        
    }
    
    
    func workoutSession(_ workoutSession: HKWorkoutSession, didChangeTo toState: HKWorkoutSessionState, from fromState: HKWorkoutSessionState, date: Date) {
        
    }
    
    func workoutSession(_ workoutSession: HKWorkoutSession, didFailWithError error: Error) {
        
    }
    
    
    let healthStore = HKHealthStore()
    var currentWorkoutSession: HKWorkoutSession?
    var workoutStartDate: Date?
    var isRunnning: Bool?
    
    weak var timer: Timer?
    var intervalSec: TimeInterval = 300.0
    
    let motionManager = CMMotionManager()
    let queue = OperationQueue()
    
    //加速度を配列に入れる処理に使う値
    var arr : [Double] = []
    
    @IBOutlet weak var Button1: WKInterfaceButton!
    @IBOutlet weak var Button2: WKInterfaceButton!
    
    var i = 0
//    var counter = -1
    
    //  機械学習用モデルの読み込み
    let model = accelD()
    
    // WatchConnectivity用
    let wcSession = WCSession.default

    override func awake(withContext context: Any?) {
        
        super.awake(withContext: context)
        
        // iPhoneとAppleWatchの連携チェック
        if WCSession.isSupported() {
            wcSession.delegate = self
            wcSession.activate()
        }
        
        if !motionManager.isDeviceMotionAvailable {
            print("Device Motion is not available.")
            return
        }
        motionManager.accelerometerUpdateInterval = 0.2 //0.2秒間隔で取得(つまり1秒間に5回)
        //  1秒したら止める処理をしないと
        motionManager.startDeviceMotionUpdates(to: queue) { (deviceMotion: CMDeviceMotion?, error: Error?) in
            if error != nil {
                print("Encountered error: \(error!)")
            }
            
            if deviceMotion != nil && self.i < 100 {
                //                sleep(UInt32(0.5))
                
                print("\(deviceMotion!.userAcceleration.x), \(deviceMotion!.userAcceleration.y), \(deviceMotion!.userAcceleration.z)")
                self.arr.append(deviceMotion!.userAcceleration.x)
                self.arr.append(deviceMotion!.userAcceleration.y)
                self.arr.append(deviceMotion!.userAcceleration.z)
                self.i = self.i + 1
                //                print("userAccelerationX = \(deviceMotion!.userAcceleration.x)")
                //                print("userAccelerationY = \(deviceMotion!.userAcceleration.y)")
                
                //                print("userAccelerationZ = \(deviceMotion!.userAcceleration.z)")
                if(self.i == 100){
                    print("+++++++++")
                    print(self.arr)
                    //ここでcoreMLRequestにarrを渡すようにしたい
                    self.coreMLRequest(array: self.arr)
                    //arrの中身を捨てる
                    self.arr.removeAll()
                    
                }
            }
        }
        // Configure interface objects here.
        
        
    }
    
    @IBAction func toggleSession() {
        
        if isRunnning == true{
            isRunnning = false
            
            
            currentWorkoutSession?.end()
            self.timer?.invalidate()
        } else {
            isRunnning = true
            
            let conf = HKWorkoutConfiguration()
            conf.activityType = .other
            
            do{
                let session = try HKWorkoutSession(healthStore: healthStore, configuration: conf)
                session.delegate = self
                workoutStartDate = Date()
                currentWorkoutSession = session
               currentWorkoutSession?.startActivity(with: workoutStartDate)
                
                self.timer?.invalidate()
                self.timer = Timer.scheduledTimer(
                    timeInterval: self.intervalSec,
                    target: self, selector: #selector(play),
                    userInfo: nil, repeats: true)
            } catch let e as NSError {
                fatalError("*** Unable to create the workout session: \(e.localizedDescription) ***")
            }
        }
        //ここで処理する
        
    }
    
    @IBAction func buttonTopped() {
        print("------------------------")
        self.i = 0
    }
    
    @objc func play(){
        
    }
    
    override func willActivate() {
        // This method is called when watch view controller is about to be visible to user
        super.willActivate()
    }
    
    override func didDeactivate() {
        // This method is called when watch view controller is no longer visible
        super.didDeactivate()
    }
    
    func coreMLRequest(array: [Double]){
        /*
        //      inputの作成
        let input = try? MLMultiArray(shape: [300], dataType: MLMultiArrayDataType.double)
        //  input typeの変換
        //  for文でなんとか
        for i in 0...299 {
            input![i] = array[i] as NSNumber
        }
        */
        

        //FirstViewControllerへ値を送る
        
        sendArraytoiPhone(Array: array)
        
        
        /*
        //--------------------------------//
        
        //  outputを作成
        let output = try! model.prediction(input: input!)
        //  outputの出力
        print("~~~~~~")
        print(input as Any)
        
        print(output.gesture)      // 1位候補のラベル
        
        print(output.classProbability) // 各クラスのラベルと確率
        
        
        //  ここから通知の実装
        if output.gesture == "1" {
            //output.gestureはstring型らしい
            //絶対1以外にする方法あったな。それはcoremltools側の問題かな
            NotificationForShake()
            print("shake")
        }else if output.gesture == "2" {
            NotificationForWave()
            print("wave")
        }else{
            print("none")
        }
        */

    }
    
    func sendArraytoiPhone(Array: [Double]){
        // iPhoneとの接続チェック
        if self.wcSession.isReachable {
            // iPhone側へ送信するデータ
            let watchMLArray: [String : [Double]] = ["Array": Array]
            // iPhone側へデータを送信
            self.wcSession.sendMessage(watchMLArray, replyHandler: {(reply) -> Void in
                // iPhone側から正常に返答があった場合
                print(reply)
            }){(error) -> Void in
                // TimeOutや型不正、データ長オーバーなど正常に返答がなかった場合
                print(error)
            }
        }
        
    }
    
    func NotificationForShake(){
        print("shake success")
        // 握手をした時の通知処理
        let content = UNMutableNotificationContent()
        content.title = "accelD"
        content.body = "握手しましたね\n仲良し度10です"
        content.sound = UNNotificationSound.default
        //ここで遅延を発生させられるけど、とりあえずtimeInterval: 0にする
        //let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 0, repeats: false)
        let request = UNNotificationRequest(identifier: "later", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
    func NotificationForWave(){
        //手を振った時の通知処理
        print("wave succeess")
        let content = UNMutableNotificationContent()
        content.title = "accelD"
        content.body = "手を振りましたね\n仲良し度20です"
        content.sound = UNNotificationSound.default
        //identifierをlaterはじゃなくするのも良さそう
        //let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 0, repeats: false)
        let request = UNNotificationRequest(identifier: "immediately", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
}
