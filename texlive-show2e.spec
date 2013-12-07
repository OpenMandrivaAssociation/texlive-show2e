# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/show2e
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-show2e
Version:	1.0
Release:	6
Summary:	Variants of \show for LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/show2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755983
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719526
- texlive-show2e
- texlive-show2e
- texlive-show2e
- texlive-show2e

