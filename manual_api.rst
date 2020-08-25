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

   No., XML タグ名, , , , , 内容, 備考
   , 第 1 階層, 第 2 階層, 第 3 階層, 第 4 階層, 属性, 
   1, xml, , , , , , <?xml version="1.0"encoding="UTF-8" ?>
   2, feed, , , , , , "http://www.w3.org/2005/Atom" 
   , , , , , , , "http://prismstandard.org/namespaces/basic/2.0/"
   , , , , , , , "http://a9.com/-/spec/opensearch/1.1/"
   , , , , , , , "ja"   
   3, feed, result
   4, feed, result, status, , , 処理結果ステータス, 0:正常 エラーの場合はエラーコード
   5, feed, result, message, , , 処理結果メッセージ, なし:正常 エラーの場合はエラーメッセージ
   6, feed, title, , , , フィード名," Volumes and Issues"
   7, feed, link, , , ,  クエリの URL
   8, feed, id, , , , クエリの URI, link 要素と同様
   9, feed, servicecd, , , , サービスコード, 巻号一覧取得は 2
   10, feed, updated, , , , 取得日時, W3CDTF 表記
   11, feed, opensearch :totalResults, , , , 検索結果総数,
   12, feed, opensearch :startIndex  , , , , 開始件数, 検索結果総数のうち、出力を開始した件数
   13, feed, opensearch :itemsPerPage, , , , 件数, 検索結果総数のうち、レスポンスに出力した件数
   14, feed, entry
   15, feed, entry, vols_title, , , 巻号一覧表示名, 予稿集の場合、開催グループ名称
   16, feed, entry, vols_title, en, , 巻号一覧表示名(英)
   17, feed, entry, vols_title, ja, , 巻号一覧表示名(日)
   18, feed, entry, vols_link, , , 目次一覧 URL
   19, feed, entry, vols_link, en, , 目次一覧 URL(英)
   20, feed, entry, vols_link, ja, , 目次一覧 URL(日)
   21, feed, entry, prism:issn , , , Print ISSN
   22, feed, entry, prism:eIssn, , , Online ISSN
   23, feed, entry, publisher, , , 学協会
   24, feed, entry, publisher, name, , 学協会名
   25, feed, entry, publisher, name, en, 学協会名(英)
   26, feed, entry, publisher, name, ja, 学協会名(日)
   27, feed, entry, publisher, url, , 学協会 URL
   28, feed, entry, publisher, url, en, 学協会 URL(英)
   29, feed, entry, publisher, url, ja, 学協会 URL(日)
   30, feed, entry, publisher, cdjournal, , 資料コード, J-STAGE で付与される資料を識別するコード
   31, feed, entry, material_title, , , 資料名
   32, feed, entry, material_title, en, , 資料名(英)
   33, feed, entry, material_title, ja, , 資料名(日)
   34, feed, entry, prism:volume, , , 巻
   35, feed, entry, cdvols, , , 分冊
   36, feed, entry, prism:number, , , 号
   37, feed, entry, prism:startingPage, href, , 開始ページ
   38, feed, entry, prism:endingPage, , , 終了ページ
   39, feed, entry, pubyear, , , 発行年, 発行年が単一の場合は YYYY、発行年が複数年の場合は YYYY-YYYY
   40, feed, entry, systemcode, , , システムコード, 1:J-STAGE 公開されているシステムのコード
   41, feed, entry, systemname, , , システム名, “J-STAGE”
   42, feed, entry, title, , , サブフィード名 Atom, フィードで表示する名称 巻号一覧表示名（日）と同様
   43, feed, entry, link, , , サブフィード URL, 目次一覧画面(日)の URL
   44, feed, entry, id, , , サブフィード ID, サブフィード URL と同様
   45, feed, entry, updated, , , 最新公開日, 号内記事の最新公開日 W3CDTF 表記

論文検索結果取得
^^^^^^^^^^^^^^^^^^^

.. csv-table::

   No., XML タグ名, , , , , 出力内容, 備考
   , 第 1 階層, 第 2 階層, 第 3 階層, 第 4 階層, 属性, 
   1, xml, , , , , , <?xml version="1.0"encoding="UTF-8" ?>
   2, feed, , , , , , "http://www.w3.org/2005/Atom"
   2, feed, , , , , , "http://prismstandard.org/namespaces/basic/2.0/"
   2, feed, , , , , , "http://a9.com/-/spec/opensearch/1.1/"
   2, feed, , , , , , "ja"
   3, feed, result
   4, feed, result, status, , ,  処理結果ステータス, 0:正常 エラーの場合はエラーコード
   5, feed, result, message, , , 処理結果メッセージ, なし:正常 エラーの場合はエラーメッセージ
   6, feed, title, , , , , "Articles"
   7, feed, link, , , , クエリの URI
   8, feed, id, , , , id, link 要素と同様
   9, feed, servicecd, , , , サービスコード, 論文検索結果取得は 3
   10, feed, updated, , , , 取得日時, W3CDTF 表記
   11, feed, opensearch:totalResults, , , , 検索結果総数
   12, feed, opensearch:startIndex  , , , , 開始件数, 検索結果総数のうち、出力を開始した件数
   13, feed, opensearch:itemsPerPage, , , , 件数, 検索結果総数のうち、レスポンスに出力した件数
   14, feed, entry
   15, feed, entry, article_title, , , 論文タイトル
   16, feed, entry, article_title, en, , 論文タイトル(英)
   17, feed, entry, article_title, ja, , 論文タイトル(日)
   18, feed, entry, article_link, , , 書誌, URL 書誌事項画面の URL
   19, feed, entry, article_link, en, , 書誌 URL(英)
   20, feed, entry, article_link, ja, , 書誌 URL(日)
   21, feed, entry, author, , , 著者名
   22, feed, entry, author, en, , 著者名(英)
   23, feed, entry, author, ja, , 著者名(日)
   24, feed, entry, cdjournal, , , 資料コード, J-STAGE で付与される資料を識別するコード
   25, feed, entry, material_title, , , 資料名
   26, feed, entry, material_title, en, , 資料名(英)
   27, feed, entry, material_title, ja, , 資料名(日)
   28, feed, entry, prism:issn, , , Print ISSN
   29, feed, entry, prism:eIssn, , , Online ISSN
   30, feed, entry, prism:volume, , , 巻
   31, feed, entry, cdvols, , , 分冊
   32, feed, entry, prism:number, , , 号
   33, feed, entry, prism:startingPage, , , 開始ページ
   34, feed, entry, prism:endingPage, , , 終了ページ
   35, feed, entry, pubyear, , , 発行年, 発行年が単一の場合は YYYY、発行年が複数年の場合は YYYY-YYYY
   36, feed, entry, joi, , , JOI
   37, feed, entry, prism:doi, , , DOI
   38, feed, entry, systemcode, , , システムコード, 1:J-STAGE 公開されているシステムのコード
   39, feed, entry, systemname, , , システム名, "J-STAGE"
   40, feed, entry, title, , , サブフィード名, Atom フィードで表示する名称 論文タイトル（日）と同様
   41, feed, entry, link, , , サブフィード URL, 書誌事項画面(日)の URL
   42, feed, entry, id, , , サブフィード ID, サブフィード URL と同様
   43, feed, entry, updated, , , 記事の公開日, 記事の公開日 W3CDTF 表記
   
   
