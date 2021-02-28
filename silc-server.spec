# TODO: start script for silcd?
Summary:	Secure Internet Live Conferencing server
Summary(pl.UTF-8):	Serwer SILC (Secure Internet Live Conferencing)
Name:		silc-server
Version:	1.1.19
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
#Source0Download: http://silcnet.org/server.html
Source0:	http://downloads.sourceforge.net/silc/%{name}-%{version}.tar.bz2
# Source0-md5:	0f82669e2a485d2b82e0995977c548f4
URL:		http://silcnet.org/server.html
BuildRequires:	pkgconfig
# silc >= 1.1
BuildRequires:	silc-toolkit-devel >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silcd is a server for SILC, Secure Internet Live Conferencing network.

%description -l pl.UTF-8
Silcd to serwer sieci SILC (Secure Internet Live Conferencing) -
bezpiecznego protokołu komunikacji na żywo przez Internet.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# interesting files packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO doc/{FAQ,example_silcd.conf,silcalgs.conf,examples}
%attr(755,root,root) %{_sbindir}/silcd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/silcalgs.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/silcd.conf
%{_mandir}/man5/silcd.conf.5*
%{_mandir}/man8/silcd.8*
