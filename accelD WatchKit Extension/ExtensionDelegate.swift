//
//  ExtensionDelegate.swift
//  accelD WatchKit Extension
//
//  Created by 藤井悠太 on 2018/10/26.
//  Copyright © 2018年 100kw. All rights reserved.
//

import WatchKit
import UserNotifications

class ExtensionDelegate: NSObject, WKExtensionDelegate {

    func applicationDidFinishLaunching() {
        // Perform any final initialization of your application.
        let center = UNUserNotificationCenter.current()
        // デリゲートを設定
        center.delegate = self;
        center.requestAuthorization(options: [.alert, .sound]) { (success, error) in
            if success {
                
                let stopAction = UNNotificationAction(identifier: "FINISH", title: "Finish", options: .foreground)
                let anotherAction = UNNotificationAction(identifier: "ANOTHER", title: "Another", options: .foreground)
                let dismissAction = UNNotificationAction(identifier: "DISMISS", title: "Dismiss", options: UNNotificationActionOptions(rawValue: 0))
                
                let notifCategory = UNNotificationCategory(identifier: "ACTIONS", actions: [stopAction,anotherAction,dismissAction], intentIdentifiers: [], options: UNNotificationCategoryOptions(rawValue: 0))
                
                center.setNotificationCategories([notifCategory])
                print("Notifications granted")
                
            } else {
                print("No authorisation")
            }
        }
    }

   
    func applicationDidBecomeActive() {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillResignActive() {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, etc.
    }

    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
        // Sent when the system needs to launch the application in the background to process tasks. Tasks arrive in a set, so loop through and process each one.
        for task in backgroundTasks {
            // Use a switch statement to check the task type
            switch task {
            case let backgroundTask as WKApplicationRefreshBackgroundTask:
                // Be sure to complete the background task once you’re done.
                backgroundTask.setTaskCompletedWithSnapshot(false)
            case let snapshotTask as WKSnapshotRefreshBackgroundTask:
                // Snapshot tasks have a unique completion call, make sure to set your expiration date
                snapshotTask.setTaskCompleted(restoredDefaultState: true, estimatedSnapshotExpiration: Date.distantFuture, userInfo: nil)
            case let connectivityTask as WKWatchConnectivityRefreshBackgroundTask:
                // Be sure to complete the connectivity task once you’re done.
                connectivityTask.setTaskCompletedWithSnapshot(false)
            case let urlSessionTask as WKURLSessionRefreshBackgroundTask:
                // Be sure to complete the URL session task once you’re done.
                urlSessionTask.setTaskCompletedWithSnapshot(false)
            case let relevantShortcutTask as WKRelevantShortcutRefreshBackgroundTask:
                // Be sure to complete the relevant-shortcut task once you're done.
                relevantShortcutTask.setTaskCompletedWithSnapshot(false)
            case let intentDidRunTask as WKIntentDidRunRefreshBackgroundTask:
                // Be sure to complete the intent-did-run task once you're done.
                intentDidRunTask.setTaskCompletedWithSnapshot(false)
            default:
                // make sure to complete unhandled task types
                task.setTaskCompletedWithSnapshot(false)
            }
        }
    }

}
extension ExtensionDelegate: UNUserNotificationCenterDelegate {
    
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.alert, .sound])
    }
}
protocol NotificationDelegate {
    func NotificationForShake()
    func NotificationForWave()
}

extension NotificationDelegate {
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
