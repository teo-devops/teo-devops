## Platform & MLOps Engineer

**K8s · Bare-Metal · Argo CD · Cilium  |  Kubeflow · MLflow  |  PySpark  |  Data Spaces (EDC, Gaia-X)  |  MSc Big Data & AI**

Diseño y opero clústeres Kubernetes sobre bare-metal —GitOps con Argo CD, red con Cilium,
backup con Velero— y los pipelines de datos y modelos que corren encima.
Trabajo sobre data spaces federados (EDC, Gaia-X). Cursando el MSc en Big Data & AI.

---

### Destacados

- **[Argo-cd-Labs](https://github.com/teo-devops/Argo-cd-Labs)** — Plano de control GitOps multi-tenant con Argo CD sobre Kubernetes bare-metal
- **[NYC-Spark-Mobility](https://github.com/teo-devops/NYC-Spark-Mobility)** — Lab distribuido NYC Taxi con arquitectura medallion, Spark 3.5 y tracking en MLflow
- **[Kubernetes-Backup-Tool](https://github.com/teo-devops/Kubernetes-Backup-Tool)** — Despliegue de Velero en cualquier cluster Kubernetes con MinIO externo como backend S3
- **[adk-agent-workflow](https://github.com/teo-devops/adk-agent-workflow)** — Labs de Google ADK: de un agente simple a workflows deterministas y multi-agente

### Repositorios por área

Cada área es un topic filtrable y una lista navegable.

| Área | Repos | Explorar |
|---|---|---|
| 🌐 **Dataspaces** | 2 públicos | [lista](https://github.com/stars/teo-devops/lists/dataspaces) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-dataspaces&type=repositories) |
| ☸️ **Kubernetes** | 4 | [lista](https://github.com/stars/teo-devops/lists/kubernetes) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-kubernetes&type=repositories) |
| 📈 **MLOps** | 5 | [lista](https://github.com/stars/teo-devops/lists/mlops) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-mlops&type=repositories) |
| 🗄️ **Data Engineering** | 5 | [lista](https://github.com/stars/teo-devops/lists/data-engineering) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-data-engineering&type=repositories) |
| 🤖 **AI Engineering** | 2 | [lista](https://github.com/stars/teo-devops/lists/ai-engineering) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-ai-engineering&type=repositories) |
| 🔧 **DevOps** | 4 | [lista](https://github.com/stars/teo-devops/lists/devops) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-devops&type=repositories) |
| 🏗️ **IaC** | 1 | [lista](https://github.com/stars/teo-devops/lists/iac) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-iac&type=repositories) |
| 🧪 **Testing** | 3 | [lista](https://github.com/stars/teo-devops/lists/testing) · [topic](https://github.com/search?q=user%3Ateo-devops+topic%3Aarea-testing&type=repositories) |

<details>
<summary><b>🌐 Dataspaces</b> — plataforma sobre Eclipse EDC</summary>

Una plataforma de dataspace con la base de [Eclipse Dataspace Components](https://github.com/eclipse-edc)
**congelada**: cada imagen se construye contra una copia inmutable de EDC derivada del tag de git
(`v<upstream>-<congelación>-<a.b.c>`), y un escenario MVD reproducible sobre KinD y Argo CD con
dos vías de datos (Envoy Gateway PULL, Bento PUSH) que hablan Data Plane Signaling.

| Repo | Stack | Qué es |
|---|---|---|
| [Connector](https://github.com/teo-devops/Connector) | `eclipse-edc` · `java` · `gradle` | Fork del connector EDC. La congelación vive en `freeze/v1.0.0-RC1-1`: versión derivada del tag, autodoc y firma adaptados a una copia congelada |
| [IdentityHub](https://github.com/teo-devops/IdentityHub) | `eclipse-edc` · `java` · `gradle` | Fork del IdentityHub EDC, misma rama de congelación y misma derivación de versión |

El resto de la plataforma —umbrella con los paquetes Maven congelados, launchers, adaptadores DPS
en Go, escenario MVD, freezer y skills de agente— está **en privado** mientras se aclara su
titularidad.

</details>

<details>
<summary><b>☸️ Kubernetes</b> — 4 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [Argo-cd-Labs](https://github.com/teo-devops/Argo-cd-Labs) | `argocd` · `continuous-delivery` · `gitops` | Plano de control GitOps multi-tenant con Argo CD sobre Kubernetes bare-metal |
| [jaeger-operator-kubernetes](https://github.com/teo-devops/jaeger-operator-kubernetes) | `jaeger` · `observability` · `operator` | Distributed tracing en Kubernetes con el Jaeger Operator |
| [kafka-strimizi-k8s](https://github.com/teo-devops/kafka-strimizi-k8s) | `kafka` · `operator` · `streaming` | Kafka sobre Kubernetes con el operador Strimzi |
| [Kubernetes-Backup-Tool](https://github.com/teo-devops/Kubernetes-Backup-Tool) | `backup` · `disaster-recovery` · `minio` | Despliegue de Velero en cualquier cluster Kubernetes con MinIO externo como backend S3 |

</details>

<details>
<summary><b>📈 MLOps</b> — 5 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [book_app.ai](https://github.com/teo-devops/book_app.ai) | `jupyter` · `machine-learning` · `python` | Proyecto de ML sobre libros: notebooks de exploracion y codigo fuente en src |
| [fashion_app_cnn](https://github.com/teo-devops/fashion_app_cnn) | `cnn` · `computer-vision` · `deep-learning` | Clasificacion de imagenes de moda con redes convolucionales |
| [NYC-Spark-Mobility](https://github.com/teo-devops/NYC-Spark-Mobility) | `docker` · `medallion-architecture` · `mlflow` | Lab distribuido NYC Taxi con arquitectura medallion, Spark 3.5 y tracking en MLflow |
| [spark_ML](https://github.com/teo-devops/spark_ML) | `jupyter` · `machine-learning` · `mllib` | Machine learning distribuido con Spark MLlib en notebooks |
| [taxi-app-ai](https://github.com/teo-devops/taxi-app-ai) | `eda` · `machine-learning` · `streamlit` | Analisis end-to-end del dataset NYC TLC con XGBoost y demo en Streamlit |

</details>

<details>
<summary><b>🗄️ Data Engineering</b> — 5 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [cluster-hadoop-docker](https://github.com/teo-devops/cluster-hadoop-docker) | `big-data` · `cluster` · `docker` | Cluster Hadoop multi-nodo dockerizado para labs de Big Data |
| [cluster-spark-docker](https://github.com/teo-devops/cluster-spark-docker) | `big-data` · `cluster` · `docker` | Cluster Spark dockerizado con notebooks para procesamiento distribuido |
| [kafka-producer](https://github.com/teo-devops/kafka-producer) | `kafka` · `producer` · `python` | Productor Kafka en Python para alimentar el lab de Strimzi |
| [Mongo_DB](https://github.com/teo-devops/Mongo_DB) | `mongodb` · `nosql` · `python` | Labs de MongoDB: modelado NoSQL y consultas desde Python |
| [Mysql-sqoop-Docker](https://github.com/teo-devops/Mysql-sqoop-Docker) | `data-ingestion` · `docker` · `hdfs` | Ingesta de MySQL a HDFS con Apache Sqoop sobre Docker |

</details>

<details>
<summary><b>🤖 AI Engineering</b> — 2 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [adk-agent-workflow](https://github.com/teo-devops/adk-agent-workflow) | `ai-agents` · `gemini` · `google-adk` | Labs de Google ADK: de un agente simple a workflows deterministas y multi-agente |
| [mcp_pg_admin_docker](https://github.com/teo-devops/mcp_pg_admin_docker) | `docker` · `mcp` · `model-context-protocol` | Lab dockerizado de PostgreSQL y pgAdmin para ensenar integracion via Model Context Protocol |

</details>

<details>
<summary><b>🔧 DevOps</b> — 4 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [Jenkins](https://github.com/teo-devops/Jenkins) | `ci-cd` · `jenkins` · `testing` | Proyecto DevOps and Cloud (UNIR): unit, service y performance testing en pipeline Jenkins |
| [minIO-docker](https://github.com/teo-devops/minIO-docker) | `docker` · `minio` · `object-storage` | Stack MinIO dockerizado como almacenamiento S3 compatible para labs |
| [nginx-crash-course](https://github.com/teo-devops/nginx-crash-course) | `learning` · `load-balancing` · `nginx` | Curso practico de Nginx: reverse proxy, load balancing y TLS |
| [todo-list-aws](https://github.com/teo-devops/todo-list-aws) | `aws` · `ci-cd` · `jenkins` | API ToDo serverless en AWS SAM con pipelines CI/CD en Jenkins |

</details>

<details>
<summary><b>🏗️ IaC</b> — 1 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [azure-infra](https://github.com/teo-devops/azure-infra) | `ansible` · `azure` · `hcl` | Infraestructura Azure con Terraform y provisioning con Ansible |

</details>

<details>
<summary><b>🧪 Testing</b> — 3 repos</summary>

| Repo | Stack | Qué es |
|---|---|---|
| [orange_e2e_testing](https://github.com/teo-devops/orange_e2e_testing) | `docker` · `e2e-testing` · `mysql` | Entorno OrangeHRM con Docker Compose para pruebas end-to-end |
| [performance-testing](https://github.com/teo-devops/performance-testing) | `docker` · `k6` · `load-testing` | API Node/Express/MongoDB dockerizada para pruebas de carga con K6 |
| [unit-testing-fizzbuzz](https://github.com/teo-devops/unit-testing-fizzbuzz) | `javascript` · `jest` · `kata` | Kata FizzBuzz con TDD y pruebas unitarias en JavaScript |

</details>

<sub>Índice generado desde los topics <code>area-*</code> de cada repo.</sub>
