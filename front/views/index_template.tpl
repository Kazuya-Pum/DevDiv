<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <title>開発者診断メーカー</title>
        <meta name="description" content="リポジトリから開発者の書き方の癖を診断">
    </head>

    <body>
        <form method="post" action="/hello" class="form-inline">
        <!-- 名前：<input type="text" placeholder="名前" name="input_text"> -->
        <div class="form-group">
            <label for="exampleInputEmail1">リポジトリ名<br></label>
            <input type="text" class="form-control" id="input_owner" name="owner" placeholder="ユーザー名">
            <input type="text" class="form-control" id="input_repo" name="repo" placeholder="リポジトリ名">
        </div>
        <div class="form-group">
            <label for="disabledSelect" class="form-label"></label>
            <select id="disabledSelect" class="form-select" name="extension">
              <option value = '.js'>.js</option>
              <option value = '.java'>.java</option>
            </select>
        </div>
        <input type="submit" value="送信する">
    </form>

    送信されたユーザー名：{{owner}}
    <br>
    送信されたリポジトリ： {{repo}}
    <br>
    送信された拡張子：{{extension}}
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <scrisspt src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>

    <!-- <textarea name="message"></textarea> -->

</html>