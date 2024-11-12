from kafka.admin import KafkaAdminClient, ConfigResource
from kafka.admin.client import ConfigResourceType

import json

try:
    admin = KafkaAdminClient(
        bootstrap_servers="deby.lan:29092",
        client_id="test-admin",
    )
    cluster_metadata = admin.describe_cluster()

    print(json.dumps(cluster_metadata))

except KeyboardInterrupt:
    admin.close()
finally:
    admin.close()
