Summary:	A tool for tunneling TCP connections over ICMP echo packets
Summary(pl.UTF-8):	Narzędzie służące do tunelowania połączeń TCP poprzez pakiety ICMP echo
Name:		ptunnel
Version:	0.71
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.cs.uit.no/~daniels/PingTunnel/PingTunnel-%{version}.tar.gz
# Source0-md5:	9b04771d4fa50abc15a6af690b81c71a
Patch0:		%{name}-Makefile.patch
URL:		http://www.cs.uit.no/~daniels/PingTunnel/index.html
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ping Tunnel is a tool for reliably tunneling TCP connections over ICMP
echo request and reply packets. It is useful for evading firewalls
that, for whatever reason, prevent outgoing TCP connections, but allow
in- and outgoing ICMP packets.

%description -l pl.UTF-8
Ping Tunnel jest narzędziem służącym do niezawodnego tunelowania
połączeń TCP poprzez pakiety ICMP echo request i ICMP echo reply. Ping
Tunnel jest użyteczny do omijania firewalli, które zabraniają
wychodzących połączeń TCP, ale pozwalają na wchodzące i wychodzące
pakiety ICMP.

%prep
%setup -q -n PingTunnel
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README LICENSE
%attr(755,root,root) %{_bindir}/ptunnel
%{_mandir}/man8/ptunnel.8*
