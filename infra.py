import pulumi
import pulumi_docker as docker
import pulumi_github as github

env = pulumi.get_stack()

my_image = docker.Image(
    name="my-nginx",
    image_name="pulumi-demo:0.0.1",
    build=docker.DockerBuild(
        dockerfile="Dockerfile"
    ),
    skip_push=True,
)

# pulumi.export('IMAGE', my_image)

# image_to_use = docker.RemoteImage("my-nginx",
#     name="pulumi-demo:0.0.1",
#     keep_locally=True
# )

container = docker.Container("my-nginx",
    name="my-nginx",
    image=my_image.base_image_name,
    ports=[{"internal":80, "external":80}]
)

# pulumi.export('CONTAINER', container)

repo = pulumi.StackReference('aldenso/github_example/'+env)

with open("Dockerfile", 'r') as f:
    filedata = f.read()

dockerfile = github.RepositoryFile("Dockerfile",
    content=filedata,
    file="Dockerfile",
    repository=repo.get_output("repo")["id"],
    branch="master"
)

# pulumi.export('DOCKERFILE', dockerfile)
