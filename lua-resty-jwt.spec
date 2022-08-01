%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.3/resty

Name: lua-resty-jwt
Summary: HMAC functions for ngx_lua and LuaJIT
Version: 0.2.3
Release: 1
URL: https://github.com/yoannguion/lua-resty-jwt
License: Apache License 2.0
Provides: JWT for ngx_lua and LuaJIT
BuildArch: noarch

%description
JWT for ngx_lua and LuaJIT


%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/evp.lua $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/jwt.lua $RPM_BUILD_ROOT%{lua_dir_resty}
cp %{_sourcedir}/lib/resty/jwt-validators.lua $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/evp.lua
%{lua_dir_resty}/jwt.lua
%{lua_dir_resty}/jwt-validators.lua

%changelog
* Mon Aug 01 2022 Yoann GUION <yoann.guion@gmail.com> - 0.2.3-1
- Initial release 0.2.3
