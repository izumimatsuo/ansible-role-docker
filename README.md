# ansible-role-docker [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-docker.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-docker)

CentOS 7 に docker, docker-compose を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名                         | デフォルト値| 説明                                    |
| ------------------------------ | ----------- | --------------------------------------- |
| docker_swarm_listen_port       | 2377        | swarm manager ポート番号                |
| docker_swarm_manager_hostnames | None        | swarm manager とする inventory ホスト名 |
