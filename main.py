from kubernetes import client, config, watch
import os

# See pod cycle https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
# Possible values are: Pending , Running, Succeeded, Failed, Unknown


def monitor_pods(namespace, state_to_monitor):
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    print(f"started to monitor {namespace}")
    w = watch.Watch()
    for event in w.stream(v1.list_pod_for_all_namespaces, namespace=namespace):
        pod = event['object']
        pod_name = pod.metadata.name
        pod_status = pod.status.phase
        event_type = event['type']
        if pod_status == state_to_monitor:
            print(f"Event: {event_type}, Pod: {pod_name}, Status: {pod_status}")


if __name__ == "__main__":
    print("indico-monitor started !")
    namespace = "default"
    state_to_monitor = os.getenv("POD_STATUS")
    if state_to_monitor == "":
        print("No state provided")
    else:
        print(f"Monitoring pods with state: {state_to_monitor}")
        monitor_pods(namespace, state_to_monitor)
