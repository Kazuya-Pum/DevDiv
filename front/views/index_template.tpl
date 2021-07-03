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
        <!-- <h1>猫の1日</h1>
        <h2>猫はかわいい<h2>
        <p>ひたすら寝ています</p>
        <p>ひたすら散歩します</p> -->
        <form method="post" action="/hello" class="form-inline">
        <!-- 名前：<input type="text" placeholder="名前" name="input_text"> -->
        <div class="form-group">
            <label for="exampleInputEmail1">リポジトリ名<br></label>
            <input type="text" class="form-control" id="exampleInputEmail1" name="input_text" placeholder="リポジトリ名">
        </div>
        <input type="submit" value="送信する">
    </form>
    <br>
    送信されたテキスト： {{text}}
    <!-- <br>
    <button type="button" class="btn btn-primary">Blue</button>
    <button type="button" class="btn btn-danger">Red</button>
    <div class="container">
    <table class="table">
    <thead>
    <tr>
    <th>#</th>
    <th>First</th>
    <th>Second</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>1</td>
    <td>apple</td>
    <td>orrange</td>
    </tr>
    </tbody>
    </table>
    </div>
 -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <scrisspt src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>

    <!-- <ul>
        <li>卵</li>
        <li>醤油</li>
    </ul> -->
    <!-- <textarea name="message"></textarea> -->

</html>