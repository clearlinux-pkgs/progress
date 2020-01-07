#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : progress
Version  : 1.5
Release  : 6
URL      : https://files.pythonhosted.org/packages/38/ef/2e887b3d2b248916fc2121889ce68af8a16aaddbe82f9ae6533c24ff0d2b/progress-1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/ef/2e887b3d2b248916fc2121889ce68af8a16aaddbe82f9ae6533c24ff0d2b/progress-1.5.tar.gz
Summary  : Shows running coreutils basic commands and displays stats
Group    : Development/Tools
License  : ISC
Requires: progress-python = %{version}-%{release}
Requires: progress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Easy progress reporting for Python
==================================
|pypi|
|demo|

%package python
Summary: python components for the progress package.
Group: Default
Requires: progress-python3 = %{version}-%{release}

%description python
python components for the progress package.


%package python3
Summary: python3 components for the progress package.
Group: Default
Requires: python3-core

%description python3
python3 components for the progress package.


%prep
%setup -q -n progress-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552839616
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
