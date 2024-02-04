### kubectl commands

get name sapces
kubectl get ns 

list pods
kubectl get pods

describe pod
kubectl describe pod <pod name>

list deploy
kubectl get deploy

### helm

list helm releases
helm ls

dry run install/upgrade helm release with chart path as current folder
helm upgrade -i <release name> . --dry-run -n <namespace name>

install/upgrade helm release with chart path as current folder
helm upgrade -i <release name> . -n <namespace name>

### k8s autoscaling 

install metrics server 
https://github.com/kubernetes-sigs/metrics-server

install VPA
https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler

HPA already part of k8s

kubectl describe HorizontalPodAutoscaler <hpa name>


sample pod with resources and limits
https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#example-1

using HPA
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

install stress to validate scaling
https://shreedhar1998.hashnode.dev/stress-command-utilization-in-linux-and-targeting-kubernetes-pods
https://lindevs.com/install-stress-command-on-ubuntu

