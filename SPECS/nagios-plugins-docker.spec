%define debug_package %{nil}

Summary:	Nagios plugin - check_docker
Name:		nagios-plugins-docker
Version:	20140504git
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		https://github.com/jsmartin/nagios-docker
Source0:	check_docker
Requires:	nagios-plugins, python-nagiosplugin, python-docker-py
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
check_docker is a Nagios plugin to check Docker's system-wide stats. The stats
returned are equivalent to the stats returned by running the docker info command.

%prep
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" check_mongodb

%setup -q -c -T

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins/check_docker

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/nagios/plugins/check_docker

%changelog
* Sun May  4 2014  Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 20140504git-1.vortex
- Initial packaging.

