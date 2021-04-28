# Soul Crabber 2

Solved by: Sowmya (@__4lph4\_\_) , Namitha (@N4m1th4_01)

This challenge was similar to it's preceding challenge `Soul Crabber` but the seed wasn't hardcoded this time. So this is a time based PRNG challenge that should be solved with proper brute force. One issue we faced was that we weren't very familiar with rust, so it took us some time. 

Here is the challenge script: 
```rust
use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;
use std::fs;
use std::io::Write;
use std::time::SystemTime;

fn get_rng() -> StdRng {
    let seed = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Time is broken")
        .as_secs();
    return StdRng::seed_from_u64(seed);
}

fn rand_xor(input : String) -> String {
    let mut rng = get_rng();
    return input
        .chars()
        .into_iter()
        .map(|c| format!("{:02x}", (c as u8 ^ rng.gen::<u8>())))
        .collect::<Vec<String>>()
        .join("");
}

fn main() -> std::io::Result<()> {
    let flag = fs::read_to_string("flag.txt")?;
    let xored = rand_xor(flag);
    println!("{}", xored);
    let mut file = fs::File::create("out.txt")?;
    file.write(xored.as_bytes())?;
    Ok(())
}
```

Output: 
```
418a5175c38caf8c1cafa92cde06539d512871605d06b2d01bbc1696f4ff487e9d46ba0b5aaf659807
```

Using time as the seed is the vulnerability here as only the last few digits are going to be changed in 2 different particular times and therefore, the seed can be bruteforced. In this problem the range to be considered was quite large.  


Here's the solution script
```rust
use rand::{Rng, SeedableRng, rngs::StdRng};
use std::fs;
use std::io::Write;
use std::time::SystemTime;
extern crate hex;
fn get_rng(seed : u64) -> StdRng {
    return StdRng::seed_from_u64(seed);
}

fn rand_xor(input : &Vec<u8>,seed:u64) -> String {
    
    let mut rng = get_rng(seed);
    return input
        .into_iter()
        .map(|c| format!("{:02x}", (c as &u8 ^ rng.gen::<u8>())))
        .collect::<Vec<String>>()
        .join("");
}


fn main() -> std::io::Result<()> {
    let mut seed=1618000000;

    let s1 = String::from("418a5175c38caf8c1cafa92cde06539d512871605d06b2d01bbc1696f4ff487e9d46ba0b5aaf659807");
    let decoded = hex::decode(s1).expect("Decoding failed");
    let mut file = fs::File::create("out.txt")?;
    while seed <1619000000{
        let  xored =  format!("{}\n", rand_xor(&decoded,seed));
        seed +=1;
        
        file.write_all(xored.as_bytes())?;
    }
    Ok(())
    }
```

Flag: `CHTB{cl4551c_ch4ll3ng3_r3wr1tt3n_1n_ru5t}` 
