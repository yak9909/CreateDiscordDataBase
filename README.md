## CreateDiscordDataBase by やくると#1951
必要なパッケージ<br>
discord.py 1.5.1  : https://github.com/Rapptz/discord.py


## このテンプレートは何？
これはやくるとが良く使うデータベースを扱うライブラリです

## このテンプレートで何が出来るの？
このテンプレートを使うと以下の様な事が可能です<br>
<br>
・ユーザーのデータを保存（全サーバー共通・そのサーバーだけ）<br>
・サーバーのデータを保存<br>
・ユーザーデータ・サーバーデータの初期設定を指定

# user.py って何？
ユーザーデータを作成・編集するためのモジュールです<br>
使い方としては

```python
from discorddb.user import User
```

でuser.pyをインポートし、

```python
User(ユーザーのClientID, サーバーID)
```

で呼び出します。このクラスを呼び出した時点で、ユーザーのデータが作られます<br>
サーバーIDを指定しなかったら data/users/ にユーザーのデータが保存されます<br>
ユーザーのデータは data/global_user_default.json を基に data/users/ に作られます<br>
サーバーIDを指定すると data/servers/user_default.json を基に data/servers/サーバーID/users/ に作られます<br>
global_user_default.json に

```json
{
  "this": "global-user"
}
```

と書いてありますが、これはUser()クラスに data という変数があり簡単に取得できるようになっています<br>
方法としては

```python
user = User(ユーザーのClientID, サーバーID)
print(user.data["this"]) # global-user
```

これを実行すると、 global-user という文字列がコンソールに出力されます<br>
書き換えも可能です

```python
user.data["this"] = "test"
user.update()
```

update()で、書き換えたデータをファイルに上書きします<br>
このメソッドを実行しないとファイルが書き換わらないので注意です

# server.py って何？
サーバーデータを作成・編集するためのモジュールです<br>
使い方は

```python
from discorddb.server import Server
```

でserver.pyをインポートし

```python
server = Server(サーバーID)
```

でServerクラスを呼び出します<br>
これもuser.pyと同じく、このクラスが呼び出された時点でディレクトリやファイルが生成されます<br>
<br>
data/servers/サーバーID/<br>
  logs/<br>
  users/<br>
  data.json<br>
<br>
このような構造になっています。<br>
users/ には User() で、グローバルを無効（サーバーIDを指定する）にして呼び出すと<br>
その場所に data/servers/user_default.json を基にユーザーのデータが生成されます<br>
Server() も User() 同様に

```python
server = Server(サーバーID)
server.data["this"] = "test"
```

で書き換え、 update() メソッドでファイルに保存します<br>
<br>
logsというディレクトリがありますが、没データです。(実装してみたら需要が無い機能だったので)<br>
リストに格納されたメッセージオブジェクトを使って

```python
server.create_log([メッセージ])
```

でログを作成することができます<br>
一個だけ作成する時もリストにしてください<br>
未完成なので動作の保証はしませんので本当にどうしても必要な場合だけ使用してください。<br>
不具合を発見したらご自身で修正して使って下さい…
