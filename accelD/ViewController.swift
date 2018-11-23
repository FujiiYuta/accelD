//
//  ViewController.swift
//  accelD
//
//  Created by 藤井悠太 on 2018/10/26.
//  Copyright © 2018年 100kw. All rights reserved.
//

import UIKit
import WatchConnectivity

class ViewController: UIViewController, WCSessionDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        activateSession()
    }

    func activateSession(){
        if WCSession.isSupported(){
            let session = WCSession.default
            session.delegate = self
            session.activate()
        }
    }
    
    func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler: @escaping ([String : Any]) -> Void){
        print("session")
        let urlString = "https://script.google.com/macros/s/AKfycbwK72G-Xv5amhUNWpI9aiP5OA0IF4XYkZbI70F543eumeGGO3OB/exec"
        let request = NSMutableURLRequest(url: URL(string: urlString)!)
        let params:[String:Any] = message
        
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        
        do{
            request.httpBody = try JSONSerialization.data(withJSONObject: params, options: .prettyPrinted)
            let task:URLSessionDataTask = URLSession.shared.dataTask(with: request as URLRequest, completionHandler: {(data,response,error) -> Void in
                let resultData = String(data: data!, encoding: .utf8)!
                print("result:\(resultData)")
                print("response:\(String(describing: response))")
            })
            task.resume()
        }catch{
            print("Error:\(error)")
            return
        }
        replyHandler(["reply" : "Done"])
    }
    
//    func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler: @escaping ([String : Any]) -> Void){
//        replyHandler(["reply" : message["OK"] as! String ])
//    }
    @available(iOS 9.3, *)
    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        print("activationDidComplete")
    }
    
    func sessionDidBecomeInactive(_ session: WCSession) {
        print("sessionDidBecomeInactive")
    }
    
    func sessionDidDeactivate(_ session: WCSession) {
        print("sessionDidDeactivate")
    }

}

