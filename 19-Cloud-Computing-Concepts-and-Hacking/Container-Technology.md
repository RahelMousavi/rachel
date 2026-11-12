
# Container Technology

## 1. Introduction to Containers

A Container is a software package that contains an application and all its dependencies, including:

- Libraries
- Configuration files
- Binaries
- Other required resources

Containers run independently of other processes in a cloud environment.

They allow applications to run across different platforms and private or public cloud environments.

### 1.1 Characteristics of Containers

- **Portability:** Applications can run across different environments.
- **Isolation:** Each container operates independently, reducing the risk of security issues spreading between applications.
- **Resource Efficiency:** Containers use fewer resources than virtual machines because they do not require a separate operating system.
- **Fast Deployment:** Containers can be created, deployed, and destroyed within seconds.

Container isolation helps limit the impact of a compromised application. However, it does not guarantee complete protection against attacks affecting the host or other containers.

## 2. Container Architecture

Container architecture describes how containerized applications are built, stored, deployed, and managed.

The process generally involves the following steps:

1. **Application Development:** Developers build applications and services into container images.
2. **Image Testing and Approval:** Container images are tested and approved before deployment.
3. **Image Storage:** Approved images are transferred to an internal or external registry or repository accessible to administrators.
4. **Deployment:** An orchestrator retrieves container images and deploys them to servers.
5. **Container Management:** The orchestrator manages container operations, including scaling, load balancing, and updates.

Examples of container orchestrators include:

- Kubernetes
- Docker Swarm

## 3. Containers vs. Virtual Machines

The course includes a comparison between containers and virtual machines.

However, the corresponding slide presents only a diagram and does not provide additional textual details.

## 4. Docker

Docker is an open-source technology used to develop, package, and run applications.

It packages applications and their dependencies into containers, allowing them to run consistently across different environments.

An application packaged as a Docker container can run in any environment that supports Docker.

### 4.1 Docker Engine

Docker Engine is a client-server application installed on the host system.

It provides the environment required to develop, deploy, and execute Docker containers.

The course slide presents the components of Docker Engine in a diagram without further textual descriptions.

Official Documentation: [Docker Documentation](https://docs.docker.com/)

## 5. Kubernetes

Kubernetes is an open-source, portable, and extensible platform originally developed by Google for managing containerized applications and microservices.

In operational environments, containers require effective management to minimize downtime.

For example, if a container fails, another container should automatically take over.

Kubernetes provides a resilient framework for managing distributed containers and supports:

- Container Management
- Deployment Patterns
- Redundancy
- Managing container availability

Official Documentation: [Kubernetes Documentation](https://kubernetes.io/docs/)

## 6. Container Management Platforms

The course introduces the following container management platforms:

- **Docker:** An open-source platform for building, packaging, and running containers.
- **Amazon ECS:** Amazon Elastic Container Service, a container management service.
- **Microsoft Azure Container Instances (ACI):** A service for running containers on Microsoft Azure.
- **Red Hat OpenShift Container Platform:** A platform for managing containerized applications.
- **Portainer:** A platform for managing container environments.
- **Rancher:** A platform for managing Kubernetes clusters.

Related Links:

- [Docker](https://www.docker.com/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Azure Container Instances](https://azure.microsoft.com/en-us/products/container-instances)
- [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)
- [Portainer](https://www.portainer.io/)
- [Rancher](https://www.rancher.com/)

## 7. Kubernetes Platforms

The course identifies the following Kubernetes platforms and technologies:

- **Kubernetes:** An open-source platform for managing containerized applications.
- **Amazon EKS:** Amazon Elastic Kubernetes Service.
- **Docker Kubernetes Service (DKS):** Listed in the course material as a Kubernetes platform.
- **Knative:** A platform built on Kubernetes for managing serverless workloads.
- **IBM Cloud Kubernetes Service:** IBM's managed Kubernetes service.
- **Google Kubernetes Engine (GKE):** Google's managed Kubernetes service.

Related Links:

- [Kubernetes](https://kubernetes.io/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [Knative](https://knative.dev/)
- [IBM Cloud Kubernetes Service](https://www.ibm.com/products/kubernetes-service)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)

## Related Links

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
- [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)

## Summary

Containers package applications together with their dependencies, providing portability, isolation, resource efficiency, and fast deployment.

Container architecture involves building images, testing them, storing them in registries, and deploying them through orchestrators.

Docker provides the technology for building and running containers, while Kubernetes manages containerized applications and supports availability, redundancy, and deployment management.

The course also introduces several container and Kubernetes management platforms, including Amazon ECS, OpenShift, Rancher, Amazon EKS, and Google Kubernetes Engine.
