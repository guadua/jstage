J-STAGE WebAPI ご利用マニュアル 
=======================================

.. warning:: 本APIは、利用規約をかならず熟読・遵守の上ご利用ください。JSTでは、APIご利用についてのご質問
   対応・サポートは行っておりません。ご利用方法等に関するお問い合わせ等にはお答えいたしかねますの
   で、本マニュアルをご参照の上、ご利用者様の責任においてご活用ください。

1. はじめに
-------------

1.1. J-STAGE WebAPI とは
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

J-STAGE に公開中の資料、巻・号、論文の情報を取得できるサービスです。J-STAGE WebAPI には、
以下のような特徴があります。

・ 資料や論文の詳細情報をメタデータ（XML 形式）で配信
・ 条件を指定して J-STAGE の情報を一度に検索が可能
・ Atom、OpenSearch に準拠しており、RSS リーダによる購読が可能

J-STAGE WebAPI の主な機能は以下のとおりです。各機能から、公開されているシステム（J-STAGE）
や、資料名などで検索した結果を取得できます。

.. csv-table::
   :header: "機能名", "説明"
   :widths: 30, 70
   
   巻号一覧取得,J-STAGE に公開されている巻・号の一覧を取得します 巻・号の発行年など、詳細な情報も取得できます
   論文検索結果取得,J-STAGE に公開されている論文の一覧を取得します 論文の公開日や書誌のメタ情報なども取得できます


1.2. 対象資料 
^^^^^^^^^^^^^^^^

J-STAGE から情報を取得できる資料は以下のとおりです。

.. csv-table::
    :header: システム名,資料名
    :widths: 30, 70

    J-STAGE, ジャーナル
    J-STAGE, 会議論文・要旨集
    J-STAGE, 研究報告・技術報告
    J-STAGE, 解説誌・一般情報誌
    J-STAGE, その他

2. 利用方法
-----------------

2.1. リクエスト
^^^^^^^^^^^^^^^^^^^

J-STAGE WebAPI へリクエストを送信します。リクエスト用 URL は、利用する機能（巻号一覧取得、
論文検索結果取得）のサービスコードと検索条件をクエリに含めて作成します。

http://api.jstage.jst.go.jp/searchapi/do?(パラメータ=値)&(パラメータ=値)&...

.. note:: ※ クエリに指定可能なパラメータの詳細は、3.リクエストパラメータを参照してください。

.. note:: ■ 補足事項

    - クエリの文字コードは UTF-8 です
    - 同一パラメータで複数の検索条件（AND 条件）を指定するときは、半角スペースで区切ります
    - URL において使用禁止である値をパラメータで指定する場合は、文字コード UTF-8 で URL エン
      コードします。

    例）資料名が「情報管理」の巻号一覧結果を取得する場合

    http://api.jstage.jst.go.jp/searchapi/do?service=2&material=%e6%83%85%e5%a0%b1%e7%ae%a1%e7%90%86

    例）資料名に「日本」と「科学」と「技術」を含む論文検索結果を取得する場合

    http://api.jstage.jst.go.jp/searchapi/do?service=3&material=%e6%97%a5%e6%9c%ac%20%e7%a7%91%e5%ad%a6%20%e6%8a%80%e8%a1%93

2.2. レスポンス
^^^^^^^^^^^^^^^^^^^

J-STAGE WebAPI へリクエストした結果を、XML 形式のレスポンスで取得します。

.. note:: ※ レスポンスから取得可能な情報の詳細は、4.レスポンスフォーマットを参照してください。

.. note:: ■ 補足事項

    - XML の文字コードは UTF-8 です
    - 検索に失敗したときは、XML 形式でエラーコード、エラーメッセージが返却されます

3. リクエストパラメータ
---------------------------

J-STAGE WebAPI に送信する HTTP リクエストの項目は以下のとおり

3.1. 巻号一覧取得
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "No.", "パラメータ", "必須 任意", "内容", "備考"
   :widths: 5, 10, 10, 40, 35

   1, service, 必須, 利用する機能を指定します, 巻号一覧取得は 2 を指定
   2, pubyearfrom, 任意, 発行年の範囲（From）を指定します, 西暦 4 桁
   3, pubyearto, 任意, 発行年の範囲（To）を指定します, 西暦 4 桁
   4, material, 任意, 資料名の検索語句を指定します, 完全一致検索
   5, issn, 任意, Online ISSNまたはPrint ISSN を指定します, 完全一致検索 XXXX-XXXX 形式
   6, cdjournal, 任意, 資料コードを指定します, J-STAGE で付与される資料を識別するコード
   7, volorder, 任意, 巻の並び順を指定します ※ , 1:昇順でソートする 2:降順でソートする 未指定の場合は 1

.. note::

   ※ 巻号一覧は巻（volorder の指定順）、分冊（昇順）、号（昇順）でソートされます。

   ※ １資料分の巻号一覧を取得できます。リクエストパラーメータに指定した条件で資料を特
   定できない場合、エラーとなります。

3.2. 論文検索結果取得 
^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "No.", "パラメータ", "必須 任意", "内容", "備考"
   :widths: 5, 10, 10, 40, 35

   1, service, 必須, 利用する機能を指定します, 論文検索結果取得は 3 を指定
   2, pubyearfrom, 任意, 発行年の範囲（From）を指定します, 西暦 4 桁
   3, pubyearto, 任意, 発行年の範囲（To）を指定します, 西暦 4 桁
   4, material, 任意, 資料名の検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   5, article, 任意, 論文タイトルの検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   6, author, 任意, 著者名の検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   7, affil, 任意, 著者所属機関の検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   8, keyword, 任意, キーワードの検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   9, abst, 任意, 抄録の検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   10, text, 任意, 全文の検索語句を指定します, 中間一致検索 大文字・小文字、全角・半角は区別しない
   11, issn, 任意, Online ISSN またはPrint ISSN を指定します, 完全一致検索 XXXX-XXXX 形式
   12, cdjournal, 任意, 資料コードを指定します, J-STAGE で付与される資料を識別するコード
   13, sortflg, 任意, 検索結果の並び順を指定します, 1:検索結果のスコア順にソートする 2:巻、分冊、号、開始ページでソートする 未指定の場合は 1
   14, vol, 任意, 巻を指定します, 完全一致
   15, no, 任意, 号を指定します, 完全一致
   16, start, 任意, 検索結果の中から取得を開始する件数を指定します※,
   17, count, 任意, 取得件数を指定します,※ 最大 1000 件まで取得可能

.. note:: ※ 検索結果のうち 1,000 件まで取得できます。1,000 件を超えて取得するときは、開始件数
   を指定し、分割してレスポンスを取得する必要があります。

   例）1,001 件目から 1,000 件分(2,000 件目)の検索結果を取得する場合

   http://api.jstage.jst.go.jp/searchapi/do?service=3&material=%e6%97%a5%e6%9c%ac%20%e7%a7%91%e5%ad%a6&start=1001&count=1000

4. レスポンスフォーマット
----------------------------

J-STAGE WebAPI から返却する XML のフォーマットは以下のとおり。

巻号一覧取得
^^^^^^^^^^^^^^^^

.. csv-table::
   :file: response_2.csv



論文検索結果取得
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: response_3.csv

   
5. エラーメッセージ
----------------------

.. csv-table::

   No., エラー内容, XML 出力内容, , 備考, 
   , , コード, メッセージ
   1, 検索結果が 0 件の場合, ERR_001, ERR_001
   2, 記事検索結果を取得したが、検索結果件数が上限件数を超えた場合, WARN_002, WARN_002
   3, J-STAGE WebAPI への同時アクセス数が制限値を超えた場合, ERR_003, ERR_003
   4, サービス区分、検索対象システム、巻順などに無効な値が設定された場合, ERR_004, ERR_004:{0}, \*{0}には、パラメータ名を出力
   5, 必須項目が未指定の場合, ERR_005, ERR_005:{0}, \*{0}には、未指定の必須項目のパラメータ名を出力
   6, 発行年に数値 4 桁以外の値が設定された場合, ERR_006, ERR_006:{0}, \*{0}には、パラメータ名を出力
   7, 記事検索結果の取得で「開始件数」と「取得件数」に数字以外が指定された場合, ERR_007, ERR_007:{0}, \*{0}には、パラメータ名を出力
   8, 「ISSN」が XXXX-XXXX フォーマット以外で指定された場合, ERR_008, ERR_008:{0}, \*{0}には、パラメータ名を出力
   9, システムの致命的なエラーが発生した場合, SYS_ERR_009, SYS_ERR_009
   10, 不正な URL が入力された場合, ERR_010, ERR_010
   11, 巻号一覧の取得で、資料名、ISSN、資料コードが一つも入力されていない場合, ERR_011, ERR_011:{0}, \*{0}には、必須項目のパラメータ名を出力
   12, 論文一覧の取得で、資料名、論文名、著者名、著者所属機関、著者キーワード、抄録、全文、ISSN、資料コード、巻、号が一つも入力されていない場合, ERR_012, ERR_012:{0}, \*{0}には、必須項目のパラメータ名を出力
   13, 巻号一覧の取得で、検索条件で資料が特定できない場合, ERR_013, ERR_013
   14, 論文検索結果の取得で、ソート使用時に資料名、ISSN のいずれも設定されていない場合, ERR_014, ERR_014


6. XML データサンプル
-----------------------

J-STAGE WebAPI から返却される XML データのサンプルは以下のとおり。

6.1. 巻号一覧 
^^^^^^^^^^^^^^^^^

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <feed xmlns="http://www.w3.org/2005/Atom"
   xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/"
   xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
   xml:lang="ja">
   <result>
   <status>0</status>
   <message/>
   </result>
   <title>Volumes and Issues</title>
   <link
   href="http://xxx.xxx.xx/do?service=2&amp;system=1&amp;pubyearfrom=&amp;pubyearto=&amp;material=%E6%83
   %85%E5%A0%B1%E7%AE%A1%E7%90%86&amp;issn=&amp;cdjournal=&amp;volorder=&amp;article=&amp;author=&amp;af
   fil=&amp;keyword=&amp;abst=&amp;text=&amp;sortflg=&amp;vol=&amp;no=&amp;start=&amp;count=100"/>

   <id>http://xxx.xxx.xx/do?service=2&amp;system=1&amp;pubyearfrom=&amp;pubyearto=&amp;material=%E6%83%8
   5%E5%A0%B1%E7%AE%A1%E7%90%86&amp;issn=&amp;cdjournal=&amp;volorder=&amp;article=&amp;author=&amp;affi
   l=&amp;keyword=&amp;abst=&amp;text=&amp;sortflg=&amp;vol=&amp;no=&amp;start=&amp;count=100</id>
   <servicecd>2</servicecd>
   <updated>2010-04-24T15:09+09:00</updated>
   <opensearch:totalResults>1</opensearch:totalResults>
   <opensearch:startIndex>1</opensearch:startIndex>
   <opensearch:itemsPerPage>1</opensearch:itemsPerPage>
   <entry>
   <vols_title>
   <en><![CDATA[Vol. 39 (1996) , No. 1]]></en>
   <ja><![CDATA[Vol. 39 (1996) , No. 1]]></ja>
   </vols_title>
   <vols_link>
   <en>http://www.jstage.jst.go.jp/browse/johokanri/39/1/_contents</en>
   <ja>http://www.jstage.jst.go.jp/browse/johokanri/39/1/_contents/-char/ja/</ja>
   </vols_link>
   <prism:issn>0021-7298</prism:issn>
   <prism:eIssn>1347-1597</prism:eIssn>
   <publisher>
   <name/>
   <url>
   <en>http://xxx.xxxx.xx.xx</en>
   <ja>http://xxx.xxxx.xx.xx</ja>
   </url>
   </publisher>
   <cdjournal>johokanri</cdjournal>
   <material_title>
   <en><![CDATA[Journal of Information Processing and Management]]></en>
   <ja><![CDATA[情報管理]]></ja>
   </material_title>
   <prism:volume>39</prism:volume>
   <prism:number>1</prism:number>
   <prism:startingPage>1</prism:startingPage>
   <pubyear>1996</pubyear>
   <systemcode>1</systemcode>
   <systemname>J-STAGE</systemname>
   <title><![CDATA[Vol. 39 (1996) , No. 1]]></title>
   <link href="http://www.jstage.jst.go.jp/browse/johokanri/39/1/_contents/-char/ja/"/>
   <id>http://www.jstage.jst.go.jp/browse/johokanri/39/1/_contents/-char/ja/</id>
   <updated>2001-04-01T00:00+09:00</updated>
   </entry>
   </feed>

論文検索結果
^^^^^^^^^^^^^^

.. code-block:: xml 

   <?xml version="1.0" encoding="UTF-8"?>
   <feed xmlns="http://www.w3.org/2005/Atom"
   xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/"
   xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
   xml:lang="ja">
   <result>
   <status>0</status>
   <message/>
   </result>
   <title>Articles</title>
   <link
   href="http://xxx.xxx.xx/do?service=3&amp;system=1&amp;pubyearfrom=&amp;pubyearto=&amp;material=%E6%83
   %85%E5%A0%B1%E7%AE%A1%E7%90%86&amp;issn=&amp;cdjournal=&amp;volorder=&amp;article=&amp;author=&amp;af
   fil=&amp;keyword=&amp;abst=&amp;text=&amp;sortflg=&amp;vol=&amp;no=&amp;start=&amp;count=100"/>

   <id>http://xxx.xxx.xx//do?service=3&amp;system=1&amp;pubyearfrom=&amp;pubyearto=&amp;material=%E6%83%
   85%E5%A0%B1%E7%AE%A1%E7%90%86&amp;issn=&amp;cdjournal=&amp;volorder=&amp;article=&amp;author=&amp;aff
   il=&amp;keyword=&amp;abst=&amp;text=&amp;sortflg=&amp;vol=&amp;no=&amp;start=&amp;count=100</id>
   <servicecd>3</servicecd>
   <updated>2010-04-24T15:13+09:00</updated>
   <opensearch:totalResults>1</opensearch:totalResults>
   <opensearch:startIndex>1</opensearch:startIndex>
   <opensearch:itemsPerPage>1</opensearch:itemsPerPage>
   <entry>
   <article_title>
   <en><![CDATA[Free Internet Access to Traditional Journals]]></en>
   <ja><![CDATA[学術雑誌のインターネット上での無料アクセス提供]]></ja>
   </article_title>
   <article_link>
   <en>http://www.jstage.jst.go.jp/article/johokanri/41/9/41_678/_article</en>
   <ja>http://www.jstage.jst.go.jp/article/johokanri/41/9/41_678/_article/-char/ja/</ja>
   </article_link>
   <author>
   <en>
   <name><![CDATA[Thomas J. Walker]]></name>
   <name><![CDATA[Soichi, transl. TOKIZANE]]></name>
   </en>
   <ja>
   <name><![CDATA[ウォーカー トーマス J.]]></name>
   <name><![CDATA[時実 象一 :訳]]></name>
   </ja>
   </author>
   <cdjournal>johokanri</cdjournal>
   <material_title>
   <en><![CDATA[Journal of Information Processing and Management]]></en>
   <ja><![CDATA[情報管理]]></ja>
   </material_title>
   <prism:issn>0021-7298</prism:issn>
   <prism:eIssn>1347-1597</prism:eIssn>
   <prism:volume>41</prism:volume>
   <prism:number>9</prism:number>
   <prism:startingPage>678</prism:startingPage>
   <prism:endingPage>694</prism:endingPage>
   <pubyear>1998</pubyear>
   <joi>JST.JSTAGE/johokanri/41.678</joi>
   <prism:doi>10.1241/johokanri.41.678</prism:doi>
   <systemcode>1</systemcode>
   <systemname>J-STAGE</systemname>
   <title><![CDATA[学術雑誌のインターネット上での無料アクセス提供]]></title>
   <link href="http://www.jstage.jst.go.jp/article/johokanri/41/9/41_678/_article/-char/ja/"/>
   <id>http://www.jstage.jst.go.jp/article/johokanri/41/9/41_678/_article/-char/ja/</id>
   <updated>2001-04-01T00:00+09:00</updated>
   </entry>
   </feed>

（ご注意）
--------------------

本マニュアルおよびシステムのご提供・ご利用にあたって、JST は一切その責を負いません。利用
者様の責任においてご活用ください。

また、バグ等のご報告を除き、機能や使い方等のお問い合わせ対応・サポート等も行っておりませ
ん。何卒ご了承くださいますようお願い申し上げます。