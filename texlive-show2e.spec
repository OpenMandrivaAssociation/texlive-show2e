Name:		texlive-show2e
Version:	15878
Release:	2
Summary:	Variants of \show for LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/show2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package aims at making debugging (especially in an
interactive way) easier, by providing \show variants suited to
LaTeX2e commands (whether with optional arguments or robust)
and environments. The variant commands also display the
internal macros used by such commands, if any. The \showcs
variant helps with macros with exotic names.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/show2e/show2e.sty
%doc %{_texmfdistdir}/doc/latex/show2e/README
%doc %{_texmfdistdir}/doc/latex/show2e/show2e-fr.pdf
%doc %{_texmfdistdir}/doc/latex/show2e/show2e.pdf
#- source
%doc %{_texmfdistdir}/source/latex/show2e/show2e.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
