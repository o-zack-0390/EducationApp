# 空欄補充型プログラミング演習問題アプリ
URL : <a href="https://o-zack-0390-educationapp-main-li79gb.streamlit.app/">空欄補充型プログラミング演習問題アプリ</a><br>
「😴」が表示されてる場合は「Yes, get this app back up!」を押して起動してください。(1分程かかります)

<h3>概要</h3>
プログラミング演習問題の一つである「空欄補充問題」を自動生成・自動採点するアプリ<br><br>

<img width="947" alt="image" src="https://user-images.githubusercontent.com/116938721/223309010-fae01554-00fd-46ad-ade9-1db9d122d63d.png">

<h3>開発言語</h3>
python3<br><br>

<h3>フレームワーク</h3>
Streamlit<br><br>

<h3>アーキテクチャ</h3>
<img width="912" alt="image" src="https://user-images.githubusercontent.com/116938721/223317062-7e392242-d1c8-4b44-b844-8507332dc51f.png">
<br><br>

<h3>使用方法(生成)</h3>
1. 実行形式「生成」を選択<br>
2. 空欄対象プログラムを選択<br>
3. 「空欄補充問題を生成」を押す<br>
4. 「ファイルをダウンロード」を押すと空欄補充問題(prob.c)がダウンロードされる<br>
<a href="https://github.com/o-zack-0390/education/blob/main/sample/7-%E6%A7%8B%E9%80%A0%E4%BD%93/prob.c">サンプル : prob.c</a><br><br>

<img width="941" alt="image" src="https://user-images.githubusercontent.com/116938721/223309208-61c707ff-a122-4d31-aae7-e8e59d560f0a.png">

<h3>使用方法(採点)</h3>
1. 以下の5種類を提出
<li>正解プログラム</li>
<li>正解プログラムの実行結果</li>
<li>空欄補充問題</li>
<li>解答者のプログラム</li>
<li>解答者のプログラムの実行結果</li>
<a href="https://github.com/o-zack-0390/EducationApp/tree/main/input_data">提出ファイルのサンプル</a><br><br>
2. 「採点を開始」を押すと採点する<br><br>
3. 「ファイルをダウンロード」を押すと採点結果がダウンロードされる<br>
<a href="https://github.com/o-zack-0390/EducationApp/blob/main/marking/student.zip">ダウンロードファイルのサンプル</a>
<br><br>


<img width="929" alt="image" src="https://user-images.githubusercontent.com/116938721/223310411-0260d4ec-2a03-4874-9aa2-8f978e1c150c.png">
<img width="920" alt="image" src="https://user-images.githubusercontent.com/116938721/223309392-365e032d-9a0a-46e3-a3f4-66297c51532b.png">
<br><br>

<h3>開発背景</h3>
大学ではプログラミング演習の授業があるが、プログラミング演習問題の作成・採点にかなりの労力が掛かっていることから開発に至った。<br><br>
<img width="944" alt="image" src="https://user-images.githubusercontent.com/116938721/223310622-7ed3d94b-b2c2-4fdb-9cfb-0532e0819d5a.png">
<br><br>

<h3>開発秘話</h3>
不適切な空欄が生成されないようにする方法を模索するのに3ヶ月掛かっており、その結果TF-IDF,正規表現,ランダム選択法を組み合わせる方法を思いついた。
<br><br>

<h3>デプロイ時のフィードバック</h3>
「自動生成」において、最初はアップロードされた.cファイルから空欄補充問題を生成する仕様にしていたが、「スマホからやる場合は.cファイルなんて持ってないよね。予め1年分の演習問題を登録しておいて選択できる方が良くない？」という意見をもらったため選択した演習問題から生成する仕様に変更している。現在はアプリ開発のプログラムなどを後輩に引き継いでおり、今年の4月からはゼミ生からもフィードバックが寄せられる。自動採点の方も選択形式で出来るようになったらもっと良くなるかもしれない。
<br><br>

<h3>参考研究</h3>
[1] 蜂巣 吉成, 吉田 敦, 阿草 清滋 : プログラムの誤り修正課題および正誤判定プログラムの自動生成<br>
[2] 柏原 昭博, 久米井 邦貴, 梅野 浩司,豊田 順一 : プログラム空欄補充問題の作成とその評価<br>
[3] 小林 勇揮, 水野 修 : N-gram IDF を利用したソースコード内の特徴的部分抽出手法
