#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdcal
Version  : 1.4
Release  : 2
URL      : https://github.com/phn/jdcal/archive/v1.4.tar.gz
Source0  : https://github.com/phn/jdcal/archive/v1.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdcal-license = %{version}-%{release}
Requires: jdcal-python = %{version}-%{release}
Requires: jdcal-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
jdcal
=====
.. _TPM: http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html
.. _Jeffrey W. Percival: http://www.sal.wisc.edu/~jwp/
.. _IAU SOFA: http://www.iausofa.org/
.. _pip: https://pypi.python.org/pypi/pip
.. _easy_install: https://setuptools.readthedocs.io/en/latest/easy_install.html

%package license
Summary: license components for the jdcal package.
Group: Default

%description license
license components for the jdcal package.


%package python
Summary: python components for the jdcal package.
Group: Default
Requires: jdcal-python3 = %{version}-%{release}

%description python
python components for the jdcal package.


%package python3
Summary: python3 components for the jdcal package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jdcal package.


%prep
%setup -q -n jdcal-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539722517
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jdcal
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/jdcal/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jdcal/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
