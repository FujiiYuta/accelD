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

class InterfaceController: WKInterfaceController, HKWorkoutSessionDelegate{
    
    let healthStore = HKHealthStore()
    var currentWorkoutSession: HKWorkoutSession?
    var workoutStartDate: Date?
    var isRunnning: Bool?
    
    weak var timer: Timer?
    var intervalSec: TimeInterval = 300.0
    
    let motionManager = CMMotionManager()
    let queue = OperationQueue()
    
    @IBOutlet weak var Button1: WKInterfaceButton!
    @IBOutlet weak var Button2: WKInterfaceButton!
    
    var i = 0
    override func awake(withContext context: Any?) {
        
        super.awake(withContext: context)
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
                self.i = self.i + 1
                //                print("userAccelerationX = \(deviceMotion!.userAcceleration.x)")
                //                print("userAccelerationY = \(deviceMotion!.userAcceleration.y)")
                //                print("userAccelerationZ = \(deviceMotion!.userAcceleration.z)")
                
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
                let session = try HKWorkoutSession(configuration: conf)
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
    
}
