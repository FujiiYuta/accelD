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


class InterfaceController: WKInterfaceController, WCSessionDelegate {

    //変数の定義など
    let motionManager = CMMotionManager()
    let queue = OperationQueue()
    
    var applicationDict = [String: String]()
    var attitude = ""
    var gravity = ""
    var rotationRate = ""
    var userAcceleration = ""
//    var userAccelerationX = ""
//    var userAccelerationY = ""
//    var userAccelerationZ = ""
    
    override func awake(withContext context: Any?) {
        // Configure interface objects here.
        print("test")
        super.awake(withContext: context)
        activateSession()
        
        if !motionManager.isDeviceMotionAvailable{
            print("Device Motion is not available")
            return
        }
        
        motionManager.startDeviceMotionUpdates(to: queue){ (deviceMotion: CMDeviceMotion?, error: Error?) in
            if error != nil{
                print("Encountered error: \(error!)")
            }
            
            if deviceMotion != nil{
                //ここを3軸の加速度にする
                self.attitude = "\(deviceMotion!.attitude)"
                self.gravity = "\(deviceMotion!.gravity)"
                self.rotationRate = "\(deviceMotion!.rotationRate)"
                self.userAcceleration = "\(deviceMotion!.userAcceleration)"
//                self.userAccelerationX = "\(deviceMotion!.userAcceleration.x)"
//                self.userAccelerationY = "\(deviceMotion!.userAcceleration.y)"
//                self.userAccelerationZ = "\(deviceMotion!.userAcceleration.z)"
            }
            //sleepって何だろ
            //これを入れないと早々にスプレッドシートが埋まりそうだから
            sleep(UInt32(0.5))
            self.sendMessage()
            
        }
    }
    
    
    
    func activateSession(){
        if WCSession.isSupported(){
            let session: WCSession = WCSession.default
            session.delegate = self 
            session.activate()
        }
    }
    func sendMessage(){
        if WCSession.default.isReachable{
            applicationDict = [
//                "userAccelerationX": userAccelerationX,
//                "userAccelerationY": userAccelerationY,
//                "userAccelerationZ": userAccelerationZ
                "attitude": attitude,
                "gravity": gravity,
                "rotationRate": rotationRate,
                "userAcceleration": userAcceleration
            ]
            
            WCSession.default.sendMessage(applicationDict, replyHandler: {(reply) -> Void in
                print(reply)
            }){(error) -> Void in
                print(error)
            }
        }
    }
    
    @available(watchOS 2.2, *)
    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        print("activationDidComplete")
    }
    
    func session(_ session: WCSession, didReceiveMessage message: [String : Any]) {
        
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
