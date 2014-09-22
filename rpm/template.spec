Name:           ros-hydro-sr-moveit-config
Version:        1.3.5
Release:        0%{?dist}
Summary:        ROS sr_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-joint-state-publisher
Requires:       ros-hydro-moveit-planners-ompl
Requires:       ros-hydro-moveit-ros-move-group
Requires:       ros-hydro-moveit-ros-visualization
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-sr-description
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-sr-description

%description
An automatically generated package with all the configuration and launch files
for using the shadowhand_motor with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 22 2014 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.3.5-0
- Autogenerated by Bloom

* Fri Sep 19 2014 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.3.4-0
- Autogenerated by Bloom

