//
//  SecondViewController.swift
//  accelD
//
//  Created by 藤井悠太 on 2019/02/05.
//  Copyright © 2019 100kw. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var imageView2: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let image = UIImage(named: "graph2")
        let image2 = UIImage(named: "sns")
        imageView.image = image
        imageView2.image = image2
    }
    
    
}
