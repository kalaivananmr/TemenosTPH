# Customer

> Source: https://docs.temenos.com/docs/Solutions/T24_Transact/Accounts/AR/Arrangement_Architecture/Property_Classes/Customer.htm

---

2. [Temenos Transact](../../../../content/T24_Transact.html)

- Retail Accounts;)

Temenos Transact

[](Constraint.htm)[Home](../ProductBuilder/Property_Classes.htm)[](Dormancy.htm)

# Customer

Updated On 07 March 2024 |  11 Min(s) read

Feedback
Summarize

The Customer Property Class is used by all products to specify all of the involved parties of an arrangement and their respective roles.

## Product lines

The following Product Lines use the Customer Property Class:

- Accounts
- Agent
- Asset Finance
- Bundle
- Deposits
- Facility
- Lending
- Relationship Pricing
- Rewards
- Safe Deposit Box

## Property Class Type

The Customer Property Class Property Class (mandatory) uses the following Property Class types:

- Dated
- Enable External
- Enable External Financial
- Enabled For Memo
- Non-Tracking

## Balance Prefix and Suffix

The Customer Property Class does not hold any balances, as it is non-financial in nature. This implies that there is no associated balance prefix.

[Attributes](#)

[Customer at Arrangement Level](#)

The customer is always defined at arrangement level. While creating the arrangement, the user enters the customer ID into AA.ARRANGEMENT.ACTIVITY. It is then displayed in the *Owner* multivalue field.

Each arrangement can have one or more legal owners defined in the *Owner* field. Additionally, other parties can be added to an arrangement with a designated role using the multivalue set of fields *Other Party.1* and *Role.1*.

The user can add any notes relating to the other party in the *Notes.1* field.

All owners and any other parties must exist in the CUSTOMER file. The user can specify the values in the *Role.1* field in the AA.PARTY.ROLE virtual table using EB.LOOKUP.

[Changing the Owner](#)

The user can change the owner of an arrangement through the LENDING-CHANGE - CUSTOMER Activity. During this change, the value in the associated *Limit Balances* field is also re-designated.

[Multiple Customers](#)

The *Customer* field available in the AA.ARRANGEMENT.ACTIVITY and AA.SIMULATION.CAPTURE is multivalue field with an associated *Customer Role* field. Multiple customers and their roles in the ownership or administration are updated in the Customer Arrangement Condition.

[Tax, Limit and General Ledger](#)

The following fields, apart from allowing the user to define multiple customers, also record the percentage ownership of each customer:

- The *Tax Liability Perc* field indicates the ownership percentage of the customer in the arrangement with respect to tax liability. Based on the percentage defined for each customer, income is split and tax is calculated.
- The *Limit Alloc Perc* field indicates the ownership percentage of the customer in the arrangement with respect to limit liability. The user can check the limit for customer for whom the field is defined..
- The *Gl Alloc Perc* field indicates the ownership percentage of the customer in the arrangement with respect to GL reporting. The customer details defined in this field is used for balance sheet reporting purposes.

Other parties who are not legal owners of the arrangement can also be specified. All owners and any other parties must exist on the CUSTOMER file. This field is part of a multivalue set with *Role.1* and *Notes.1* fields.

The user can indicate whether the limit customers are jointly and severally liable. In this case, more than one customer is involved in the limit and all of them are liable for the entire loan amount. This *JS Liable* field is enabled for the user input only if the new limit key is allowed in the system (that is, *Key Type* field in LIMIT.PARAMETER should be TXN.REF).

[Customer Role](#)

The user defines customer roles and characteristics in the arrangement. The user must ensure to specify a role to each customer in the arrangement. The role assigned to a customer describes the responsibilities and rights of the customer in the arrangement. As it is a mandatory field, if there is no user input, the system defaults the role as owner.

The field can be updated using the AA.CUSTOMER.ROLE record.

Customer roles are defined for the following:

- The *Beneficial Owner* field indicates whether the customer(s) pertaining to the role is a beneficial owner of the arrangement. The beneficial owner is a legal owner of the arrangement and is responsible for the contract with the bank.
  - For single customer ownership, the role is defaulted as beneficial owner.
  - For joint ownership, there has to be at least one customer with their role configured to be a beneficial owner.
- The *Limit Customer* field defines whether the customer associated with the role requires a limit. The options available are Yes or No. If the *Beneficial Owner* is set as Yes, then it is mandatory that the *Limit Customer* is also set as Yes.
- The user can indicate the taxable customer in the *Customer* field.

  The multivalue set is applicable only for taxable customers and not for general ledger and limit customers.
- The *Maximum Tax Liability Percentage* field indicates the tax liability percentage for taxable customers.
- The user can edit the default tax percentage at arrangement level.
- Each customer in the account can have different preferential pricing available. It is possible to ascertain and assign the best pricing available for the account.
- The *Delivery Customer* field defines whether the customer associated with the role receives delivery messages.
- *App Format* is a four-digit acronym which has the following roles:
  - This acronym is used by De Customer Preferences to generate the appropriate De Product and specify the Carrier or Address Preferences for different delivery messages.
  - The acronym used in *App Format* need not be unique. This allows the usage of the same acronym in two different customer roles, such as Whole Loan Guarantor and Shortfall Guarantor. These roles are different from liability perspective but can share the acronym as GUTR to ease setup of the preferences.
- *Gl Customer* defines whether the customer associated with the role can drive the composition of general ledger key.
- It is possible to indicate whether Relationship pricing arrangements pertaining to the Customer with a specific role have to be taken into consideration at the time of creating an arrangement. This is achieved by flagging the *Rel Pricing Avail* field.

[Storage of Arrangement Information](#)

The user can use the AA.CUSTOMER.ROLE table to define roles.

The *Maintain Info* attribute is used to control how the arrangement info gets updated in the AA tables. The following are the three options in the *Maintain Info* attribute.



1. Comprehensive or Blank

   This is the default option in which the arrangement information is maintained in AA Arrangement, AA Customer Arrangement and AA CRA tables. It is applicable for both beneficial owner(BO) and non-beneficial owner roles.
2. High Volume

   This option is apt for customer roles like corporate insurers and guarantors who provide guarantee for a high volumes of accounts but are not directly involved in the arrangement. This is permitted only for non-BO roles like the guarantor, attorney and third party. When chosen, the account information is maintained only in the AA.MASS.CUSTOMER.ARRANGEMENT table. The arrangement information is not maintained in Customer Arrangement and CRA tables.

   Since the CRA table is not updated in the High Volume option, the customers using this role are not considered for pricing.
3. Basic Info

   In this option, only the basic account information is maintained in the Arrangement table. Information is not maintained in the Customer Arrangement, Mass Customer Arrangement and CRA tables. This option is permitted only for non-BO customer roles.

The following table summarises the storage of information in different tables based on the *Maintain Info* options chosen:

| *Maintain Info* Options | AA Customer Arrangement | AA Mass Customer Arrangement | AA Customer Related Arrangements | AA Arrangement |
| --- | --- | --- | --- | --- |
| Comprehensive | Yes | - | Yes | Yes |
| High Volume | - | Yes | - | Yes |
| Basic Info | - | - | - | Yes |

The illustration of an arrangement created by the user with multiple customer roles is detailed below.

A Comprehensive role is created in the AA.CUSTOMER.ROLE application (Applicant) as shown below.



A High Volume type is created in the AA.CUSTOMER.ROLE application (Guarantor) as shown below.



A Basic Info type is created in the AA.CUSTOMER.ROLE application (Legal) as shown below.



A jointly owned current account is opened, using the three roles created by the bank, namely: Applicant (John), Guarantor (International Insurance), Legal (KPMG). The customer IDs are 190521, 190522 and 190523 respectively.



Storage of information in different tables is illustrated below.

[AA Arrangement](#)

The AA.ARRANGEMENT table is updated for all the three customer roles as shown below.



[AA Customer Arrangement](#)

The AA.CUSTOMER.ARRANGEMENT table is updated for 190521(Comprehensive) as shown below.



For a High volume role, the AA.CUSTOMER.ARRANGEMENT table for customer 190252 is updated with *Mass Customer Update*. This field is the indicator that the information is stored in the AA.MASS.CUSTOMER.ARRANGEMENT table.



For Basic Info role, the arrangement information is not stored in the AA.CUSTOMER.ARRANGEMENT table.



[AA Mass Customer Arrangement](#)

The AA.MASS.CUSTOMER.ARRANGEMENT table is updated only for customer 190252 which used the High Volume role.



The AA.MASS.CUSTOMER.ARRANGEMENT table is not updated for customer 190251 which used the Comprehensive role.



The AA.MASS.CUSTOMER.ARRANGEMENT table is not updated for customer 190251 which used the Basic Info role.



[AA Customer Related Arrangements](#)

The AA.CUSTOMER.RELATED.ARRANGEMENTS table is updated for customer 190251 (John) using the Comprehensive role.



AA.CUSTOMER.RELATED.ARRANGEMENTS parameter configuration is a pre-requisite for CRA updates.

For the customer 190252, High volume role is assigned, hence information is not updated in the AA.CUSTOMER.RELATED.ARRANGEMENTS table.



For the customer 190253, Basic Info is assigned, hence information is not updated in the AA.CUSTOMER.RELATED.ARRANGEMENTS table.



## Periodic Attribute Classes

There are no periodic attribute classes associated with Customer Property Class.

## Actions

The Customer Property Class supports the UPDATE action.

| Action Name | Description |
| --- | --- |
| UPDATE | It is initiated manually and allows the user to change any of the customer attributes. The user initiates this action as part of the New-Arrangement and Update-Customer Activities. Any modification to the static customer data results in changes to related data within other applications. For example, Account. |

## Accounting Events

The Customer Property Class does not perform actions that generate accounting events.

## Limits Interaction

The Customer Property Class does not perform any actions that impact the limits system.



In this topic

- [Customer](#Customer)

- [Product lines](#Productlines)
- [Property Class Type](#PropertyClassType)
- [Balance Prefix and Suffix](#BalancePrefixandSuffix)
- [Periodic Attribute Classes](#PeriodicAttributeClasses)
- [Actions](#Actions)
- [Accounting Events](#AccountingEvents)
- [Limits Interaction](#LimitsInteraction)


Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Thursday, April 16, 2026 10:03:56 PM IST