---
title: Create a brand-new property
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Set up a unique property file you'll need for each of your <<COMPANY_NICKNAME>> products.

1. Use the **+Create ** button in the top navigation bar and select **Property**. You can also go to <<PORTAL_ICON_ROOT>> <<CHAR_MENU_DELIMITER>> **CDN** <<CHAR_MENU_DELIMITER>> **Properties**, and then click **+New Property**.

2. Select the <<COMPANY_NICKNAME>> product you want to use.

3. Name your property and select a group it will belong to. 

> 📘 
> 
> A property name is a unique identifier in Akamai systems. We recommend not reusing a property name, even from a deleted property, unless it is for a property of the same type. Reusing a name also reuses the original associated _arlfile_, which can cause system conflicts when the type changes.

4. Select the rule format you want to use for the property's rule tree.

> 📘 
> 
> <<COMPANY_NICKNAME>> often modifies behaviors and matches, each time deploying a new internal version of the feature. By default, the Property Manager interface in <<PORTAL_NICKNAME>> uses the latest available feature versions. In the interest of stability, some Property Manager solutions like [Includes](doc:includes-overview) or [API](ref:api) don't support this system of selective updates for each feature. Instead, the feature sets are simply versioned as a whole. These versions, which update infrequently, are known as rule formats.

5. Optionally, select the **Hostname bucket** checkbox to create a property with a [hostname bucket](doc:configure-hostname-buckets). Enable this option for a streamlined process to add and remove hostnames without incrementing property versions.

6. Click **Next**. 

# What's next

You should now see the [Property Manager Editor](doc:know-your-around#editor-view) where you can start setting up version 1 of your new property. For the first step in the process, let's [redirect users to edge servers](doc:redirect-users-edge-servers) by creating a new **Property Hostnames** entry.

<div align=center>
<img src="https://techdocs.akamai.com/property-manager/img/pm-editor-initial-view-v1.jpg" width="417" height="440"/>
</div>