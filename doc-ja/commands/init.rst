=================
``init`` コマンド
=================

:doc:`./lint` の実行に必要な設定を生成するコマンド。

概要
====

``docan`` の動作に必要な初期設定の組み立てを行う。

フローチャート
==============

.. blockdiag::

    diagram {
      orientation = portrait;
      edge_layout = flowchart;

      begin [shape = flowchart.terminator];
      end [shape = flowchart.terminator];

      check [shape = flowchart.condition];
      prompt [shape = box];
      generate [shape = flowchart.input];

      d [shape=none];

      begin -> check -> prompt -> generate -> end;
      check -> d -> generate -> end;
    }

.. list-table:: 各フローの概要
    :widths: 10, 20, 70
    :header-rows: 1

    * - プロセス
      - 回数
      - 概要
    * - ``check``
      - 1回のみ
      - 引数の内容精査。不足が無いかの整理などを実施する。
    * - ``prompt``
      - 最大1回
      - 項目確認。引数に応じて設定の基本情報を受け付ける。
    * - ``generate``
      - 1回
      - 設定出力。項目に従って設定内容を出力する。

フロー内詳細
============

``check``
---------

引数の詳細チェック。

引数に従い出力プロセスを決定する。
出力プロセスに対して不足があるかもここで判定する。

``prompt``
----------

出力設定の充足処理。

``check`` において出力プロセスへの不足があった場合に、
プロンプトを表示しつつ項目の入力を促す。

``generate``
------------

出力処理。

引数と ``prompt`` の結果を組み合わせて設定項目を用意する。
用意した項目をもとに出力を行うが、出力先自体も項目に依存する。
