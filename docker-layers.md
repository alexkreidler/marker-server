https://docker.io/v2/nvidia/cuda/manifests/12.4.1-cudnn-runtime-ubuntu22.04

https://registry-1.docker.io/v2/nvidia/cuda/manifests/12.4.1-cudnn-runtime-ubuntu22.04


```
docker buildx build --builder cloud-alexkreidler-default-builder -f docker/Dockerfile.modal --push --tag alexkreidler/marker-server:1.0.2-modal --platform linux/amd64 .
```
Need platform cause on mac it defaults to linux/arm64?

Cache does work, only took 20 seconds to run the build adding chmod.

```

al@Als-MacBook-Air ~> docker  --log-level=debug  manifest inspect -v nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04
time="2024-12-08T17:47:41-05:00" level=debug msg="endpoints for docker.io/nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04: [{false https://registry-1.docker.io v2 false true true 0x1400040b520}]"
time="2024-12-08T17:47:41-05:00" level=debug msg="not continuing on error (*errors.fundamental) docker.io/nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04 is a manifest list"
time="2024-12-08T17:47:41-05:00" level=debug msg="endpoints for docker.io/nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04: [{false https://registry-1.docker.io v2 false true true 0x1400040a680}]"
[
	{
		"Ref": "docker.io/nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04@sha256:db2b1629f7b905dba40d5f3f55e2681c457c0e48910360fa421db7017377dda5",
		"Descriptor": {
			"mediaType": "application/vnd.docker.distribution.manifest.v2+json",
			"digest": "sha256:db2b1629f7b905dba40d5f3f55e2681c457c0e48910360fa421db7017377dda5",
			"size": 2418,
			"platform": {
				"architecture": "arm64",
				"os": "linux"
			}
		},
		"Raw": "ewogICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuZGlzdHJpYnV0aW9uLm1hbmlmZXN0LnYyK2pzb24iLAogICAic2NoZW1hVmVyc2lvbiI6IDIsCiAgICJjb25maWciOiB7CiAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5jb250YWluZXIuaW1hZ2UudjEranNvbiIsCiAgICAgICJkaWdlc3QiOiAic2hhMjU2OjMzZjI3ZDIyYTUyZGQwYzFhZDE4YTA4NmQ1Nzg1MDJjNzZkNmE0YjMyMjI3ZmEzZWRiYjM2MTdlZjMwNDY2ODAiLAogICAgICAic2l6ZSI6IDE0MDkzCiAgIH0sCiAgICJsYXllcnMiOiBbCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6NzAxMDRjZDU5ZTJhNDQzYjlkOWExM2E2YmNlM2JiZjFhZTc4MjYxYzQxOThhNDBiZjY5ZDZlMDUxNWFiZTA2YSIsCiAgICAgICAgICJzaXplIjogMjczNTk1NTEKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1NjozNWU2ZGQ1NWI2NDFhOTFjN2QyYmYzYmMzMWI4MTMwMmQ2MWEyM2RmNjQ3M2Y5ZmFkNjA4YzgxZjg4NTJkYjZmIiwKICAgICAgICAgInNpemUiOiA0NTc0NzcwCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6NTZjOGNkYjQyZDI0ZTZlN2NkNTQ1YTQxODI5ODkxYWQ1MmMyNWUyZWM4ODNiYzRiZTdkODFiNzgwNGRmYWM1MiIsCiAgICAgICAgICJzaXplIjogMzgxNDA5CiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6MjI3NDg1Njg5NjdmZTY5NjMyOGE3NDBkNjQ0NTMxYWYxNTA0ZjE1YzUzMjQ1YThkZTQxYWI1N2IyNGJmYmIxYSIsCiAgICAgICAgICJzaXplIjogMTg3CiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6NTZkYzg1NTAyOTM3NTFhMTYwNGU5N2FjOTQ5Y2ZhZTgyYmEyMGNiMmEyOGUwMzQ3MzdiYWZkNzM4MjU1OTYwOSIsCiAgICAgICAgICJzaXplIjogNjg4NgogICAgICB9LAogICAgICB7CiAgICAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5pbWFnZS5yb290ZnMuZGlmZi50YXIuZ3ppcCIsCiAgICAgICAgICJkaWdlc3QiOiAic2hhMjU2OmI5NzIzN2YzMTE2NjBkY2MzOTMwMTNjZjU4ZDc4MDRjMTk5ZmUwY2I0ZDZmMDI2NTA5NmFiOGRkZjcwNmU3ZjYiLAogICAgICAgICAic2l6ZSI6IDEzNzM0NDU4MzYKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1NjoyZTg4MjUxNWZhZDkyZjU1MTI2OGUzYmVjZDRkZjg2MGFlNGEwZDAxNWRmMzBlYThhYmI2Y2UyMjM0MjE3ZjQwIiwKICAgICAgICAgInNpemUiOiA2Mzc1NgogICAgICB9LAogICAgICB7CiAgICAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5pbWFnZS5yb290ZnMuZGlmZi50YXIuZ3ppcCIsCiAgICAgICAgICJkaWdlc3QiOiAic2hhMjU2OmUzN2JkYmZjNTVlZGM1MjlhOGQ0N2I3MTVmMzA2NTFmNzhhNTZjMGI1OTEyMmUyMzhiMmViYTY5NWRmODVmNDkiLAogICAgICAgICAic2l6ZSI6IDE2ODQKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1Njo0YzYwYjVlNzMwN2U4NmZhODIyMDNiMGMyMjdkODAwMWRjZTFmYzQ4MDRmZDQ5YmJiMmQ0MmY2YTVhODA1OTU0IiwKICAgICAgICAgInNpemUiOiAxNTIzCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6Njc1ZTBiNTY3MTU3ZDVkZTFmMjlhZGEwMWYyNmNhZDIzNmE0ZjVkNGI3MGQyNjAwMGIwYmYxNGE0YzkxYTZiMSIsCiAgICAgICAgICJzaXplIjogNjY4NzI1NjE5CiAgICAgIH0KICAgXQp9",
		"SchemaV2Manifest": {
			"mediaType": "application/vnd.docker.distribution.manifest.v2+json",
			"schemaVersion": 2,
			"config": {
				"mediaType": "application/vnd.docker.container.image.v1+json",
				"digest": "sha256:33f27d22a52dd0c1ad18a086d578502c76d6a4b32227fa3edbb3617ef3046680",
				"size": 14093
			},
			"layers": [
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:70104cd59e2a443b9d9a13a6bce3bbf1ae78261c4198a40bf69d6e0515abe06a",
					"size": 27359551
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:35e6dd55b641a91c7d2bf3bc31b81302d61a23df6473f9fad608c81f8852db6f",
					"size": 4574770
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:56c8cdb42d24e6e7cd545a41829891ad52c25e2ec883bc4be7d81b7804dfac52",
					"size": 381409
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:22748568967fe696328a740d644531af1504f15c53245a8de41ab57b24bfbb1a",
					"size": 187
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:56dc8550293751a1604e97ac949cfae82ba20cb2a28e034737bafd7382559609",
					"size": 6886
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:b97237f311660dcc393013cf58d7804c199fe0cb4d6f0265096ab8ddf706e7f6",
					"size": 1373445836
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:2e882515fad92f551268e3becd4df860ae4a0d015df30ea8abb6ce2234217f40",
					"size": 63756
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:e37bdbfc55edc529a8d47b715f30651f78a56c0b59122e238b2eba695df85f49",
					"size": 1684
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:4c60b5e7307e86fa82203b0c227d8001dce1fc4804fd49bbb2d42f6a5a805954",
					"size": 1523
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:675e0b567157d5de1f29ada01f26cad236a4f5d4b70d26000b0bf14a4c91a6b1",
					"size": 668725619
				}
			]
		}
	},
	{
		"Ref": "docker.io/nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04@sha256:0bb88834d973ca1b450fcc2a05333c6fe45510bee289912a5391274c351c4a4d",
		"Descriptor": {
			"mediaType": "application/vnd.docker.distribution.manifest.v2+json",
			"digest": "sha256:0bb88834d973ca1b450fcc2a05333c6fe45510bee289912a5391274c351c4a4d",
			"size": 2420,
			"platform": {
				"architecture": "amd64",
				"os": "linux"
			}
		},
		"Raw": "ewogICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuZGlzdHJpYnV0aW9uLm1hbmlmZXN0LnYyK2pzb24iLAogICAic2NoZW1hVmVyc2lvbiI6IDIsCiAgICJjb25maWciOiB7CiAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5jb250YWluZXIuaW1hZ2UudjEranNvbiIsCiAgICAgICJkaWdlc3QiOiAic2hhMjU2OmEwMjlhODc3ZjdlMzNhZGE0ZTRlYWFkZjA4NWZmNWFkNTE3OTk0ZjJmMGU0MTY4NDVmZjEwOWVjZTIzMzFmNGIiLAogICAgICAic2l6ZSI6IDE0Mjg2CiAgIH0sCiAgICJsYXllcnMiOiBbCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6M2M2NDUwMzFkZTI5MTdhZGU5M2VjNTRiMTE4ZDVkM2U0NWRlNzJlZjU4MGI4ZjQxOWE4Y2RjNDFlMDFkMDQyYyIsCiAgICAgICAgICJzaXplIjogMjk1MzM0MTkKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1NjowZDY0NDhhZmY4ODk0NWVhNDZhMzdjZmU0MzMwYmRiMGFkYTIyODI2OGI4MGRhNjI1OGEwZmVjNjMwODZmNDA0IiwKICAgICAgICAgInNpemUiOiA0NjIzNjk0CiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6MGE3Njc0ZTNlOGZlNjlkY2Q3ZjE0MjRmYTI5YWEwMzNiMzJjNDIyNjlhYWI0NmNiZTk4MThmOGRkNzE1NDc1NCIsCiAgICAgICAgICJzaXplIjogNTc1OTM2NDAKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1NjpiNzFiNjM3Yjk3YzVlZmI0MzViOTk2NTA1OGFkNDE0ZjA3YWZhOTlkMzIwY2YwNWU4OWYxMDQ0MWVjMWJlY2Y0IiwKICAgICAgICAgInNpemUiOiAxODUKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1Njo1NmRjODU1MDI5Mzc1MWExNjA0ZTk3YWM5NDljZmFlODJiYTIwY2IyYTI4ZTAzNDczN2JhZmQ3MzgyNTU5NjA5IiwKICAgICAgICAgInNpemUiOiA2ODg2CiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6ZWM2ZDVmNmM5ZWQ5NGQyZWUyZWVhZjA0OGQ5MDI0MmFmNjM4MzI1ZjU3Njk2OTA5ZjE3MzdiMzE1OGQ4MzhjZiIsCiAgICAgICAgICJzaXplIjogMTM3NDI5NTQwMQogICAgICB9LAogICAgICB7CiAgICAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5pbWFnZS5yb290ZnMuZGlmZi50YXIuZ3ppcCIsCiAgICAgICAgICJkaWdlc3QiOiAic2hhMjU2OjQ3Yjg1MzlkNTMyZjU2MWNhYzZkN2ZiOGVlMmY0NmM5MDJiNjZlNGE2MGIxMDNkMTk3MDE4Mjk3NDJhMGQxMWUiLAogICAgICAgICAic2l6ZSI6IDY0MDQ3CiAgICAgIH0sCiAgICAgIHsKICAgICAgICAgIm1lZGlhVHlwZSI6ICJhcHBsaWNhdGlvbi92bmQuZG9ja2VyLmltYWdlLnJvb3Rmcy5kaWZmLnRhci5nemlwIiwKICAgICAgICAgImRpZ2VzdCI6ICJzaGEyNTY6ZmQ5Y2MxYWQ4ZGVlNDdjYTU1OTAwMzcxNGQ0NjJmNGViNzljYjYzMTVhMjcwODkyN2MyNDBiODRkMDIyYjU1ZiIsCiAgICAgICAgICJzaXplIjogMTY4NAogICAgICB9LAogICAgICB7CiAgICAgICAgICJtZWRpYVR5cGUiOiAiYXBwbGljYXRpb24vdm5kLmRvY2tlci5pbWFnZS5yb290ZnMuZGlmZi50YXIuZ3ppcCIsCiAgICAgICAgICJkaWdlc3QiOiAic2hhMjU2OjgzNTI1Y2FlZWIzNTk3MzFmODY5ZjFlZTg3YTMyYWNkZmRkNWVmYjhhZjRjYWIwNmQ4ZjRmZGNmMWYzMTdkYWEiLAogICAgICAgICAic2l6ZSI6IDE1MjMKICAgICAgfSwKICAgICAgewogICAgICAgICAibWVkaWFUeXBlIjogImFwcGxpY2F0aW9uL3ZuZC5kb2NrZXIuaW1hZ2Uucm9vdGZzLmRpZmYudGFyLmd6aXAiLAogICAgICAgICAiZGlnZXN0IjogInNoYTI1NjpiZGY1ZWI0ZmQzMmM5MGE1MjI3OWIyYmZkN2VhMGQ3MWRhNzA4MTEyODQ0MDEwNDlhMzgwNzQ2MTI1ZGI4NDJjIiwKICAgICAgICAgInNpemUiOiA2NzAxMDM5NjMKICAgICAgfQogICBdCn0=",
		"SchemaV2Manifest": {
			"mediaType": "application/vnd.docker.distribution.manifest.v2+json",
			"schemaVersion": 2,
			"config": {
				"mediaType": "application/vnd.docker.container.image.v1+json",
				"digest": "sha256:a029a877f7e33ada4e4eaadf085ff5ad517994f2f0e416845ff109ece2331f4b",
				"size": 14286
			},
			"layers": [
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:3c645031de2917ade93ec54b118d5d3e45de72ef580b8f419a8cdc41e01d042c",
					"size": 29533419
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:0d6448aff88945ea46a37cfe4330bdb0ada228268b80da6258a0fec63086f404",
					"size": 4623694
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:0a7674e3e8fe69dcd7f1424fa29aa033b32c42269aab46cbe9818f8dd7154754",
					"size": 57593640
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:b71b637b97c5efb435b9965058ad414f07afa99d320cf05e89f10441ec1becf4",
					"size": 185
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:56dc8550293751a1604e97ac949cfae82ba20cb2a28e034737bafd7382559609",
					"size": 6886
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:ec6d5f6c9ed94d2ee2eeaf048d90242af638325f57696909f1737b3158d838cf",
					"size": 1374295401
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:47b8539d532f561cac6d7fb8ee2f46c902b66e4a60b103d19701829742a0d11e",
					"size": 64047
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:fd9cc1ad8dee47ca559003714d462f4eb79cb6315a2708927c240b84d022b55f",
					"size": 1684
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:83525caeeb359731f869f1ee87a32acdfdd5efb8af4cab06d8f4fdcf1f317daa",
					"size": 1523
				},
				{
					"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
					"digest": "sha256:bdf5eb4fd32c90a52279b2bfd7ea0d71da70811284401049a380746125db842c",
					"size": 670103963
				}
			]
		}
	}
]
al@Als-MacBook-Air ~> curl https://registry-1.docker.io/v2/nvidia/cuda/manifests/12.4.1-cudnn-runtime-ubuntu22.04
{"errors":[{"code":"UNAUTHORIZED","message":"authentication required","detail":[{"Type":"repository","Class":"","Name":"nvidia/cuda","Action":"pull"}]}]}
```