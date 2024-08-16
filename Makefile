.PHONY: build redeploy install destroy

build:
	docker build -t indico-monitor .

redeploy:
	kubectl rollout restart deployment/indico-monitor

reapply:
	kubectl apply -f pod-monitor/templates

install:
	helm install indico-monitor ./indico-monitor

destroy:
	helm uninstall indico-monitor
