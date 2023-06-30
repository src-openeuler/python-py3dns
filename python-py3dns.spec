%global _empty_manifest_terminate_build 0
Name:		python-py3dns
Version:	3.2.1
Release:	2
Summary:	Python 3 DNS library
License:	Python License
URL:		https://launchpad.net/py3dns
Source0:	https://mirrors.nju.edu.cn/pypi/web/packages/8a/b7/bd0fca1b330527ccf5f47a586900797dd1e054909f7d4c5e287de8b3fe59/py3dns-3.2.1.tar.gz
Patch0:         python3-py3dns-handle-absent-resolv.patch
BuildArch:	noarch


%description
Python 3 DNS library:

%package -n python3-py3dns
Summary:	Python 3 DNS library
Provides:	python-py3dns
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
%description -n python3-py3dns
Python 3 DNS library:

%package help
Summary:	Development documents and examples for py3dns
Provides:	python3-py3dns-doc
%description help
Python 3 DNS library:

%prep
%autosetup -n py3dns-3.2.1 -p1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-py3dns -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Mar 29 2023 lichaoran <pkwarcraft@hotmail.com> - 3.2.1-2
- add patch to handle missing of resolv.conf

* Thu Mar 09 2023 Python_Bot <Python_Bot@openeuler.org> - 3.2.1-1
- Package Spec generated
