//
//  ViewController.swift
//  accelD
//
//  Created by 藤井悠太 on 2018/10/26.
//  Copyright © 2018年 100kw. All rights reserved.
//

import UIKit
import WatchConnectivity
import UserNotifications
//  機械学習用ライブラリ
import CoreML

class FirstViewController: UIViewController, WCSessionDelegate {
    
    //  機械学習用モデルの読み込み
    let model = accelD()
    
    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        if let error = error {
            print("Activation failed with error: \(error.localizedDescription)")
            return
        }
        print("Watch activated with state: \(activationState.rawValue)")
    }
    
    func sessionDidBecomeInactive(_ session: WCSession) {
        // To support multiple watches.
        print("WC Session did become inactive.")
    }
    
    func sessionDidDeactivate(_ session: WCSession) {
        // To support multiple watches.
        WCSession.default.activate()
        print("WC Session did deactivate.")
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        if (WCSession.isSupported()) {
            let session = WCSession.default
            session.delegate = self
            session.activate()
        }
        
    }
    
    func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler: @escaping ([String : Any]) -> Void) {
       //呼ばれてない
        print("aaa")
        
        //      inputの作成
        let input = try? MLMultiArray(shape: [300], dataType: MLMultiArrayDataType.double)
        let array = message["Array"] as! [Double]
        //  input typeの変換
        for i in 0...299 {
            
            input![i] = array[i] as NSNumber
        }
        
        print("test")
        print(input as Any)
        
        //  outputを作成
        let output = try! model.prediction(input: input!)
        
        //  outputの出力
        print("~~~~~~")
//        print(input as Any)
        
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
        
        replyHandler(["reply" : "OK"])
//        print("bbb")
    }
    
    func NotificationForShake(){
        print("shake success")
        // 握手をした時の通知処理
        let content = UNMutableNotificationContent()
        content.title = "accelD"
        content.body = "握手しましたね!!\n仲良し度+10です!"
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
        content.body = "手を振りましたね!!\n仲良し度+20です!"
        content.sound = UNNotificationSound.default
        //identifierをlaterはじゃなくするのも良さそう
        //let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 0, repeats: false)
        let request = UNNotificationRequest(identifier: "immediately", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
}

