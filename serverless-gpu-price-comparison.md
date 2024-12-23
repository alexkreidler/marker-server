## Runpod

[Source](https://www.runpod.io/serverless-gpu)

| Memory | GPU Models              | Flex  | Active |
| ------ | ----------------------- | ----- | ------ |
| 80 GB  | A100                    | $2.72 | $2.17  |
| 80 GB  | H100 PRO                | $5.59 | $4.47  |
| 48 GB  | A6000, A40              | $1.22 | $0.85  |
| 48 GB  | L40, L40S, 6000 Ada PRO | $1.90 | $1.33  |
| 24 GB  | L4, A5000, 3090         | $0.69 | $0.48  |
| 24 GB  | 4090 PRO                | $1.10 | $0.77  |
| 16 GB  | A4000, A4500, RTX 4000  | $0.58 | $0.40  |

## Modal

Modal primarily uses Oracle Cloud Infrastructure (OCI) for its underlying GPU and compute resources. [1](https://www.oracle.com/customers/modal-labs/)

[Source](https://modal.com/pricing)

| GPU Models         | Memory | Per Second | Per Hour |
| ------------------ | ------ | ---------- | -------- |
| Nvidia H100        | 80 GB  | $0.001267  | $4.56    |
| Nvidia A100, 80 GB | 80 GB  | $0.000944  | $3.40    |
| Nvidia A100, 40 GB | 40 GB  | $0.000772  | $2.78    |
| Nvidia A10G        | 24 GB  | $0.000306  | $1.10    |
| Nvidia L4          | 24 GB  | $0.000222  | $0.80    |
| Nvidia T4          | 16 GB  | $0.000164  | $0.59    |

| Resource               | Cost Per Second | Cost Per Hour |
| ---------------------- | --------------- | ------------- |
| Physical core (2 vCPU) | $0.000038       | $0.135        |
| Memory (per GiB)       | $0.00000667     | $0.024        |

```
Runner failed with exception: container exited successfully but never requested inputs
```

Doesn't actually get the inputs or start the endpoint properly? https://github.com/modal-labs/modal-client/issues/2625


```

Runner failed with exit code: 127
python: 1: ./docker/entrypoint.sh: not found

```

## Beam

Pros: Their core [serverless GPU framework is open-source](https://github.com/beam-cloud/beta9), so you can self-host it or debug/contribute to fix issues you may run into.

[Source](https://www.beam.cloud/pricing)

| GPU Models   | Per Hour |
| ------------ | -------- |
| T4 GPU       | $0.54    |
| RTX 4090 GPU | $0.69    |
| A10G GPU     | $1.05    |
| A100-40 GPU  | $2.75    |

| Resource       | Cost Per Hour |
| -------------- | ------------- |
| CPU (per core) | $0.190        |
| RAM (per GB)   | $0.020        |
| File Storage   | Included      |

```
Exiting worker due to startup error
from marker.converters.pdf import PdfConverter
ModuleNotFoundError: No module named 'marker'
```

Doesn't use the Python interpreter from the virtualenv I set up in docker: https://github.com/beam-cloud/beta9/issues/774

## Baseten

[Source](https://www.baseten.co/pricing/)

| Instance Type    | GPU Model | VRAM   | vCPUs | RAM     | Cost Per Minute | Cost Per Hour |
| ---------------- | --------- | ------ | ----- | ------- | --------------- | ------------- |
| T4x4x16          | T4        | 16 GiB | 4     | 16 GiB  | $0.01052        | $0.6312       |
| L4x4x16          | L4        | 24 GiB | 4     | 16 GiB  | $0.01414        | $0.8484       |
| A10Gx4x16        | A10s      | 24 GiB | 4     | 16 GiB  | $0.02012        | $1.2072       |
| A100x12x144      | A100      | 80 GiB | 12    | 144 GiB | $0.10240        | $6.1440       |
| H100x26x234      | H100      | 80 GiB | 26    | 234 GiB | $0.16640        | $9.9840       |
| H100MIG:3x13x117 | H100 MIG  | 40 GiB | 13    | 117 GiB | $0.08250        | $4.9500       |

## Fly.io

[Source](https://fly.io/docs/about/pricing/#gpus-and-fly-machines)

| GPU Model     | Memory | Cost Per Hour |
| ------------- | ------ | ------------- |
| A10           | 24 GB  | $1.50         |
| L40S          | 48 GB  | $1.25         |
| A100 40G PCIe | 40 GB  | $2.50         |
| A100 80G SXM  | 80 GB  | $3.50         |

```
Error: failed to provision seed volumes: failed to create volume: Your organization does not have enough trust to access GPU machines. Please contact billing@fly.io to remove the restriction.
```

## Cerebrium

[Source](https://www.cerebrium.ai/pricing)

| GPU       | Memory | Cost per Second | Cost per Hour |
| --------- | ------ | --------------- | ------------- |
| T4        | 16GB   | $0.000164       | $0.5904       |
| L4        | 24GB   | $0.000222       | $0.7992       |
| A10       | 24GB   | $0.000306       | $1.1016       |
| L40s      | 48GB   | $0.000750       | $2.70         |
| A100 40GB | 40GB   | $0.000772       | $2.7792       |
| H100      | 80GB   | $0.001267       | $4.5612       |
| A100 80GB | 80GB   | $0.001553       | $5.5908       |

## Overview

| GPU Model               | Memory | Runpod Flex | Runpod Active | Modal | Beam  | Baseten | Fly.io | Cerebrium |
| ----------------------- | ------ | ----------- | ------------- | ----- | ----- | ------- | ------ | --------- |
| H100                    | 80 GB  | $5.59       | $4.47         | $4.56 | -     | $9.98   | -      | $4.56     |
| A100                    | 80 GB  | $2.72       | $2.17         | $3.40 | -     | $6.14   | $3.50  | $5.59     |
| A100                    | 40 GB  | -           | -             | $2.78 | $2.75 | -       | $2.50  | $2.78     |
| H100 MIG                | 40 GB  | -           | -             | -     | -     | $4.95   | -      | -         |
| A6000, A40              | 48 GB  | $1.22       | $0.85         | -     | -     | -       | -      | -         |
| L40, L40S, 6000 Ada PRO | 48 GB  | $1.90       | $1.33         | -     | -     | -       | $1.25  | $2.70     |
| A10G                    | 24 GB  | -           | -             | $1.10 | $1.05 | $1.21   | $1.50  | -         |
| L4                      | 24 GB  | $0.69       | $0.48         | $0.80 | -     | $0.85   | -      | $0.80     |
| A5000, 3090             | 24 GB  | $0.69       | $0.48         | -     | -     | -       | -      | -         |
| 4090 PRO                | 24 GB  | $1.10       | $0.77         | -     | $0.69 | -       | -      | -         |
| A4000, A4500, RTX 4000  | 16 GB  | $0.58       | $0.40         | -     | -     | -       | -      | -         |
| T4                      | 16 GB  | -           | -             | $0.59 | $0.54 | $0.63   | -      | $0.59     |