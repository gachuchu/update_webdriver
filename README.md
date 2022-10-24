# webdriverをブラウザバージョンにあわせて適当にダウンロードする

webdriver_managerを使えばいいのに、劣化した車輪を再発明したくてしょうがなくて作った  
後悔はしていないけど公開はしてみた。とりあえずChromeだけ  
普通の人はwebdriver_managerを使おう  

## <span style="color:red">免責事項&注意事項</span>

自分の環境・使い方で動けばいいや。で作っているので検証、デバッグが圧倒的に足りていないです。  
本プロジェクトを利用した、または利用できなかった、その他いかなる場合において一切の保障は行いません。  
自己の責任のもとでご利用ください。

## 使い方の一例

1. python -m venv venv で作った仮想環境で動かす前提です
1. update_webdriver.batの`CHROME_PATH`の値を自分の環境にあわせて修正
1. update_webdriver.batの`call venv\Scripts\activate.bat & py update_webdriver.py`の引数に   
webdriverをダウンロードするパスを指定する（デフォルトは1階層上のフォルダ）
1. update_webdriver.batを実行

## 補足

なんかあれば書く
