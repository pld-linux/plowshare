#
# TODO: make shell scripts executable
#
%define		svn	r1542
Summary:	Command line (CLI) designed for popular file-sharing websites
Name:		plowshare
Version:	%{svn}
Release:	0.1
License:	GPL v3+
Group:		Applications
Source0:	http://plowshare.googlecode.com/files/%{name}-SVN-%{version}-snapshot.tar.gz
# Source0-md5:	0216a9addc638e8acc9df601daaa4f57
URL:		http://code.google.com/p/plowshare/
Requires:	libcaca-img
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
plowshare is a command line (CLI) application designed for popular
file-sharing websites (aka Hosters). With plowshare, you will be able
to download or upload files and manage remote folders and link
deletion.

%prep
%setup -q -n %{name}-SVN-%{version}-snapshot

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/plowdel
%attr(755,root,root) %{_bindir}/plowdown
%attr(755,root,root) %{_bindir}/plowlist
%attr(755,root,root) %{_bindir}/plowup
%{_datadir}/%{name}
%{_mandir}/man1/plow*.1*
