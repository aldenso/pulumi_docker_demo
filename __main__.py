import pulumi
import infra

pulumi.export('image', infra.my_image)
pulumi.export('container', infra.container)
pulumi.export('dockerfile', infra.dockerfile)