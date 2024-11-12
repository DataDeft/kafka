# Kafka

## Python install

```bash
deactivate
rm -rf venv/
/usr/bin/python3 -vm venv venv
. venv/bin/activate.fish
pip install uv
uv pip install kafka-python black
```


## Docker compose

```bash
docker compose -f docker-compose.yml up
```

```bash
docker compose -f docker-compose.yml down --rmi all
```

## Commands

- version

```bash
./opt/bin/kafka-topics.sh --bootstrap-server deby.lan:29092 --version
3.8.0
```

- list topics

```bash
./opt/bin/kafka-topics.sh \
--bootstrap-server deby.lan:29092 \
--list

__consumer_offsets
test-topic
```

- producer

```bash
./opt/bin/kafka-console-producer.sh \
--topic test-topic \
--bootstrap-server deby.lan:29092
```

- consumer


```bash
./opt/bin/kafka-console-consumer.sh \
--topic test-topic \
--from-beginning \
--bootstrap-server deby.lan:29092
```

- create topic

```bash
./opt/bin/kafka-topics.sh \
--bootstrap-server deby.lan:29092 \
--create \
--topic test-topic \
--partitions 3 \
--replication-factor 3
```

- cluster id

```bash
./opt/bin/kafka-cluster.sh cluster-id \
--bootstrap-server deby.lan:29092
Cluster ID: test-cluster
```

- perf test

```bash
./opt/bin/kafka-producer-perf-test.sh \
--topic test-topic \
--num-records 10000 \
--throughput 1000 \
--record-size 100 \
--producer-props bootstrap.servers=deby.lan:29092

4986 records sent, 997.0 records/sec (0.10 MB/sec), 8.4 ms avg latency, 502.0 ms max latency.
10000 records sent, 995.619275 records/sec (0.09 MB/sec), 10.21 ms avg latency, 502.00 ms max latency, 8 ms 50th, 26 ms 95th, 56 ms 99th, 88 ms 99.9th.
```

```bash
./opt/bin/kafka-consumer-perf-test.sh \
--bootstrap-server deby.lan:29092 \
--topic test-topic \
--group test-group \
--messages 1000 \
--timeout 6000
start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
WARNING: Exiting before consuming the expected number of messages: timeout (6000 ms) exceeded. You can use the --timeout option to increase the timeout.
2024-10-17 18:44:19:332, 2024-10-17 18:44:25:443, 0.0000, 0.0000, 0, 0.0000, 666, 5445, 0.0000, 0.0000
```

## Python


- https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
- https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html