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

class InterfaceController: WKInterfaceController {
    let motionManager = CMMotionManager()
    let queue = OperationQueue()
    @IBOutlet weak var Button1: WKInterfaceButton!
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
    @IBAction func buttonTopped() {
        print("------------------------")
        self.i = 0
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
