from mmap import ALLOCATIONGRANULARITY
from .github import Repository
from .analysis import Analysis

def execute(owner, repo, extension):
    repository = Repository(owner, repo, extension)
    analysis = Analysis(repository)

    var_mean_len = analysis.var_mean_len()
    var_max_len = analysis.var_max_len()
    var_num = analysis.var_num()
    var_kind = analysis.var_kind()
    var_num_par = var_kind / var_num # 種類数/使用数
    
    if var_num_par > 0.8:
        if var_mean_len > 8:
            vec_type = '変数乱立'
            word_type = '心配性'
            message_type = '無駄な変数がないか確認してみよう！'
        elif var_mean_len > 4:
            vec_type = '変数乱立'
            word_type = 'コンスタント'
            message_type = '変数名の長さはGOOD！ただし，宣言した変数は使ってみよう！'
        else:
            vec_type = '変数乱立'
            word_type = '大雑把な'
            message_type = '意味のない変数名を付けていない？誰でも分かるような変数名を意識しよう！'
    elif var_num_par > 0.4:
        if var_mean_len > 8:
            vec_type = '変数適材適所'
            word_type = '心配性'
            message_type = '変数名が短くすることで，より見やすいコードになるかも！'
        elif var_mean_len > 4:
            vec_type = '変数適材適所'
            word_type = 'コンスタント'
            message_type = 'この調子で他の人が見やすいコードを意識しよう！'
        else:
            vec_type = '変数適材適所'
            word_type = '大雑把な'
            message_type = '自分だけ分かる変数名を付けていない？誰でも分かるような変数名を意識しよう！'
    else:
        if var_mean_len > 8:
            vec_type = '変数多重人格'
            word_type = '心配性'
            message_type = 'もしかすると変数に予期せぬ値が入ってるかも．ときには変数を分けて宣言することも大事！'
        elif var_mean_len > 4:
            vec_type = '変数多重人格'
            word_type = 'コンスタント'
            message_type = '変数の付け方はGOOD!ただし，同じ変数の使い過ぎには注意！'
        else:
            vec_type = '変数多重人格'
            word_type = '大雑把な'
            message_type = 'あなたのコードは人に見せれますか？自分はそうは思いません．'
    # vec_type = "vec_type"   #TODO
    # word_type = "word_type"
    most_used = analysis.get_most_used_word()

    res = f'<center>変数情報</center>使用数：{var_num}<br>種類数：{var_kind}<br>平均文字数：{round(var_mean_len, 2)}<br>最大文字と長さ：{var_max_len[0]}, {var_max_len[1]}<br><b>{vec_type}型の{word_type}な変数{most_used}の使い手<br>{message_type}</b>'
    # res = f'{vec_type}型の{word_type}な{most_used}の使い手'
    #message = f'{vec_type}型の{word_type}な{most_used}の使い手<br>{message_type}'

    return {'res': res,'text': ' '.join(repository.words)}