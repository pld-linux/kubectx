Summary:	kubectx + kubens: Power tools for kubectl
Name:		kubectx
Version:	0.6.3
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/ahmetb/kubectx/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bc7054bf9bf62aacd0e404ded83f0b07
URL:		https://github.com/ahmetb/kubectx
Requires:	kubectl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Switch faster between clusters and namespaces in kubectl.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p kubectx $RPM_BUILD_ROOT%{_bindir}
install -p kubens $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md LICENSE
%attr(755,root,root) %{_bindir}/kubectx
%attr(755,root,root) %{_bindir}/kubens
