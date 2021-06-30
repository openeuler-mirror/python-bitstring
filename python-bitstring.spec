%global srcname bitstring

Name:           python-%{srcname}
Version:        3.1.7
Release:        1
Summary:        Simple construction, analysis and modification of binary data

License:        MIT
URL:            https://github.com/scott-griffiths/%{srcname}
Source0:        %{srcname}-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

%description
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.


%prep
%autosetup -n %{srcname}-%{srcname}-%{version}

dos2unix README.rst release_notes.txt
sed -i '1{s|^#!/usr/bin/env python||}' %{srcname}.py


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m nose -w test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst release_notes.txt
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-%{python3_version_nodots}*.pyc
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jun 30 2021 Lianguo Wang <wanglianguo@kylinos.cn> - 3.1.7
- Add src.
