[project]
name = gogs
version = 0.11.43
vendor = gogs.io
homepage = https://gogs.io
groups = app/dev,app/prod,app/co
description = A painless self-hosted Git service.


%build
PREFIX="/opt/gogs/gogs"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "gogs-{{.project__version}}.linux_amd64.tar.gz" ]; then
    wget "https://dl.gogs.io/{{.project__version}}/gogs_{{.project__version}}_linux_amd64.tar.gz" gogs-{{.project__version}}.linux_amd64.tar.gz
fi
if [ ! -d "gogs" ]; then
    tar -zxf gogs-{{.project__version}}.linux_amd64.tar.gz
fi

cd gogs

cp -rp public    {{.buildroot}}/
cp -rp scripts   {{.buildroot}}/
cp -rp templates {{.buildroot}}/
cp -rp gogs      {{.buildroot}}/
cp -rp LICENSE   {{.buildroot}}/
cp -rp README.md {{.buildroot}}/

chmod +x {{.buildroot}}/gogs
strip -s {{.buildroot}}/gogs
mkdir -p {{.buildroot}}/var/repos
mkdir -p {{.buildroot}}/var/log
mkdir -p {{.buildroot}}/custom/conf

cd {{.inpack__pack_dir}}/deps
rm -rf gogs

%files
misc/

