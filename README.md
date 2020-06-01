# pulumi_docker_demo

Demo de pulumi con docker

```sh
pulumi version
```

```shell
v2.2.1
```

## Requerimientos

* Python3.
* Pulumi CLI ([pulumi](https://www.pulumi.com/docs/reference/cli/)).
* Cuenta de Github ([github](https://github.com/)).
* Organizacion de Github ([organization_github](https://github.com/organizations/plan)).
* Token de Github con permisos sobre organizaciones (admin:org, delete_repo, repo), se puede acceder desde Icono de user - settings - Developer settings - Personal Access Tokens).

Nota: este demo tiene dependencia con [github_demo](https://github.com/aldenso/pulumi_github_demo)

Normalmente el proyecto se crea como sigue:

```sh
pulumi new -d "Mi proyecto docker" --dir docker_example -n docker_example -s production -y python
```

Nota: No realizar, ya el repositorio tiene el contenido final

Se instalan las librerias faltantes.

```sh
cd docker_example
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Se crean los archivos para el programa con la configuracion deseada.

Nota: No realizar, ya el repositorio tiene el contenido final

Crear el stack inicial.

```sh
pulumi stack init production
```

Se ingresan las configuraciones necesarias para el programa.

```sh
pulumi config set --secret github:token TUTOKENDEGITHUB
pulumi config set github:organization TUORGDEGITHUB
```

Se realiza un preview del despliegue.

```sh
pulumi preview
```

Finalmente se realiza el despliegue.

```sh
pulumi up --yes
```
