use rsautogui::mouse;
use std::thread;
use std::time::Duration;
use ureq;

#[derive(Debug, serde::Serialize, serde::Deserialize)]
struct ReturnType {
    active: bool,
}

fn main() {
    let mut prev = false;

    loop {
        let value = ureq::get("https://button.pgarguflow.com/get/0")
            .call()
            .expect("Failed to hit button api")
            .into_json::<ReturnType>()
            .unwrap();
        println!("poll");
        if prev != value.active {
            mouse::click(mouse::Button::X2);
            println!("flipped");
        }
        prev = value.active;
        thread::sleep(Duration::from_millis(250));
    }
}
