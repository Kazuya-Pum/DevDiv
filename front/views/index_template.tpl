<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>猫の実態</title>
        <meta name="description" content="猫の好きなもの，日々の生活をご紹介">
    </head>

    <body>
        <!-- <h1>猫の1日</h1>
        <h2>猫はかわいい<h2>
        <p>ひたすら寝ています</p>
        <p>ひたすら散歩します</p> -->
        <form method="post" action="/hello">
        名前：<input type="text" placeholder="名前" name="input_text">
        <input type="submit" value="送信する">
    </form>
    <br>
    送信されたテキスト： {{text}}
    </body>

    <!-- <ul>
        <li>卵</li>
        <li>醤油</li>
    </ul> -->
    <!-- <textarea name="message"></textarea> -->

</html>