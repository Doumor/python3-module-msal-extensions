%define pypi_name msal-extensions

%def_without check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Microsoft Authentication extensions for MSAL Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/AzureAD/microsoft-authentication-extensions-for-python/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif


BuildArch: noarch

Source: %name-%version.tar

%description
The Microsoft Authentication Extensions for Python offers secure mechanisms for client applications to perform cross-platform token cache serialization andpersistence. It gives additional support to the Microsoft Authentication Library	for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the SerializableTokenCache to perform cache serialization. You can read more about this in the MSAL Python documentation. Developers are required to implement their own cache persistance across multiple platforms and Microsoft Authentication Extensions makes this simpler.

%prep
%setup

# Remove DOS line endings
sed "s|\r||g" README.md >README.md.new && \
touch -r README.md README.md.new && \
mv README.md.new README.md

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest


%files
%doc README.md
%python3_sitelibdir/msal_extensions/
%python3_sitelibdir/msal_extensions-%version.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
