# Introduction to Country Validation

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PSINCV/Country_Validation/Misc/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Country Validation > Introduction

- Country Validation;)
  - [Introduction](../../Country_Validation/Misc/Introduction.htm)
  - [Configuration](../../Country_Validation/Misc/Configuration.htm)
  - [Working with](../../Country_Validation/Misc/Working_with.htm)
  - [Tasks](../../Country_Validation/Misc/Tasks.htm)
  - [Outputs](../../Country_Validation/Misc/Outputs.htm)

Payments

# Introduction to Country Validation

Updated On 08 October 2024 |
 13 Min(s) read

Feedback
Summarize

Many countries have issued payment regulations for international payments received by them (international inward remittances). These regulations are formulated to support anti-money laundering controls and improve payment transparency (for regulatory controls and monitoring purposes) as per the rules and guidelines laid out by the respective country’s foreign exchange regulatory agencies.

For example, the Central Bank of UAE has mandated the following information for any payment coming into UAE.

- IBAN must have 23 characters (AEXX + 19 digits)
- Purpose of payment must be stated
- Ordering customer’s name and address must be provided

In such cases, it is the responsibility of the bank (who initiates a payment) to validate that the cross-border payments comply with the above set of requirements when the payment is sent to UAE.

This module provides a framework to define the rules and validate the payment data against the respective rules. This module provides the following features,

- Capture or configure the validation rules per country group, country, and payment currency.
- Receive country validation requests from Transact applications, validate them against the respective rule table and respond with an ‘OK’ or ‘Not OK’ response.

This module supports configuring the rules for a country group (where a list of countries is part of the group), country (destination country), and currency (payment currency irrespective of destination country).

- Country group definition does not restrict configuring only the standard international country group. Any group (including the standard group namely EEA) having a common set of rules can be configured in a record instead of duplicating the rules for each country.
- License for the Country Specific Validations module is PSINCV.

## Defining Field Validation

Banks can define the following validations for a field:

- Mandatory field (for example, a country mandates that the creditor name and address must be provided)
- Format of the value in a specific field (for example, the creditor account number must be 10 digits)
- Pre-defined set of values that a specific field can accept (for example, purpose code must not be equal to PENS and SALA)
- Rule based on some condition (for example, category purpose code must be SALA when the payment amount is greater than 20,000 USD)

## Setting up Rule

The user ensures the following when setting up rules in the Country Rules table:

- Record ID must be a valid ISO country code, any country group or valid ISO currency code, followed by the effective date.
- Pre-defined set of keywords to be used for defining the rules.
- Format of the field value.
- Fixed set of values for a field.
- Conditional set of fields on whose values the rule is dependent.
- Error or override text to be returned when the rules are not met.

## Pre-defined Keywords

Each field or message tag names are assigned a keyword that must be used while defining the rules table. When the application sends a request to the Country Rules table, the payment object must be mapped to the respective keywords as defined in the rules table.

The following table has the list of keywords.

| Keywords | Description |
| --- | --- |
| Creditor Agent Country | Country of Creditor's bank (Account with Bank) |
| Transaction Currency | ISO currency code of the payment amount |
| Transaction Amount | Payment amount expressed in the transaction currency |
| Transfer Type | Customer or Bank transfer. The supported values are C and B |
| Source Module | Source or module from where the request is initiated |
| Product | Specific product name under the source module |
| Channel | Output channel of the payment |
| Creditor Account | Identification of the account of the creditor |
| Creditor IBAN | International bank account number of the creditor |
| Creditor Name | Name of the creditor |
| Creditor BIC | Business identification code of the creditor |
| Creditor Street Name | Street name of the creditor |
| Creditor PO Box | Numbered box in a post office, assigned to the creditor |
| Creditor Postal Code | Postal code of the creditor |
| Creditor Town Name | Creditor's location name within the town |
| Creditor Residency | Country of residence of the Creditor |
| Creditor Agent BIC | BIC of Creditor's bank (Account with Bank) |
| Creditor Agent Clearing System ID | Identification of the creditor agent’s national clearing system |
| Creditor Agent Clearing Code | National clearing code of Creditor's bank (Account with Bank) |
| Creditor Agent Name | Name of the creditor agent |
| Creditor Agent Account | Identification of the account of the creditor agent |
| Creditor Agent IBAN | IBAN of the creditor agent |
| Creditor Agent Town Name | Creditor's agent town name |
| Debtor Account | Identification of the account of the debtor |
| Debtor Name | Name of the debit party |
| Debtor Town Name | Debtor party's town name |
| Debtor Country | Debtor party’s country |
| Creditor LEI | Legal entity identification of the creditor |
| Creditor Type | Type of the Creditor, such as organisation or individual |
| Creditor Bank Party ID | Creditor's bank party identification (that is, organisation identification with the scheme code as BANK) |
| Creditor Central Bank Number | Creditor's central bank identification number (the organisation identification with the scheme code as CBID) |
| Creditor Clearing Number | Creditor's clearing identification number (the organisation identification with the scheme code as CHID) |
| Creditor Incorporation Number | Creditor's certificate of incorporation number (the organisation identification with the scheme code as CINC) |
| Creditor Country ID Code | Creditor's country identification code (the organisation identification with the scheme code as COID) |
| Creditor Organisation Customer Number | Creditor's organisation customer number (the organisation identification with the scheme code as CUST) |
| Creditor Numbering System | Creditor's data universal numbering system (the organisation identification with the scheme code as DUNS) |
| Creditor Employer Number | Creditor's employer identification number (the organisation identification with the scheme code as EMPL) |
| Creditor GS1GLN ID | Creditor's GS1GLN identifier (the organisation identification with the scheme code as GS1G) |
| Creditor SIREN Code | Creditor's SIREN identification code (the organisation identification with the scheme code as SREN) |
| Creditor SIRET Code | Creditor's SIRET identification code (the organisation identification with the scheme code as SRET) |
| Creditor Organisation Tax Number | Creditor's organisation tax identification number (the organisation identification with the scheme code as TXID) |
| Creditor Alien Number | Creditor's alien registration number (the private identification with the scheme code as ARNU) |
| Creditor Passport Number | Creditor's passport number (the private identification with the scheme code as CCPT) |
| Creditor Private Customer Number | Creditor's private customer identification number (the private identification with the scheme code as CUST) |
| Creditor License Number | Creditor's driver license number (the private identification with the scheme code as DRLC) |
| Creditor Employee Number | Creditor's employee identification number (the private identification with the scheme code as EMPL) |
| Creditor National Number | Creditor's national identity number (the private identification with the scheme code as NIDN) |
| Creditor Security Number | Creditor's social security number (the private identification with the scheme code as SOSE) |
| Creditor Private Tax Number | Creditor's private tax identification number (the private identification with the scheme code as TXID) |
| Creditor Telephone Number | Creditor's telephone number (the private identification with the scheme code as TELE) |
| Creditor Organisation ID Proprietary 1 | Creditor's Organisation Identification 1 with the scheme proprietary |
| Creditor Organisation ID Proprietary 2 | Creditor's Organisation Identification 2 with the scheme proprietary |
| Creditor Private ID Proprietary 1 | Creditor's Private Identification 1 with the scheme proprietary |
| Creditor Private ID Proprietary 2 | Creditor's Private Identification 2 with the scheme proprietary |
| Creditor Address Line Unstructured | Creditor address line unstructured |
| Debtor Address Line Unstructured | Debtor address line unstructured |
| Creditor Agent Address Line Unstructured | Creditor Agent address line unstructured |
| Remittance Information Unstructured | Remittance information in an unstructured form |
| Remittance Information Structured Line 1 | Remittance information 1 in a structured form |
| Remittance Information Structured Line 2 | Remittance information 2 in a structured form |
| Remittance Information Structured Line 3 | Remittance information 3 in a structured form |
| Instruction for Creditor Agent 1 | Information line 1 for the Creditor's bank |
| Instruction for Creditor Agent 2 | Information line 2 for the Creditor's bank |
| Category Purpose Code | Code of the category purpose |
| Payment Purpose | Purpose of the payment |
| Generic Information | Configuration for information override. This keyword must be used only to configure the override text. |
| Ultimate Debtor Name | Ultimate debtor name |
| Ultimate Debtor Town | Ultimate debtor town name in structured address |
| Ultimate Debtor Country | Ultimate debtor country |
| Ultimate Creditor Name | Ultimate creditor name |
| Ultimate Creditor Town | Ultimate creditor town name in structured address |
| Ultimate Creditor Country | Ultimate creditor country |
| Instruction for Next Agent 1 | Instruction for next agent line 1 |
| Instruction for Next Agent 2 | Instruction for next agent line 2 |
| Instruction for Next Agent 3 | Instruction for next agent line 3 |
| Instruction for Next Agent 4 | Instruction for next agent line 4 |
| Service Level Code | Service level code |
| Local Instrument Code | Local instrument code |
| Regulatory Debt Cred Report | Regulatory Debtor Creditor Report |
| Regulatory Authority Name | Regulatory reporting information - authority name |
| Regulatory Authority Country | Regulatory reporting information - authority country |
| Regulatory Reporting Type | Regulatory reporting information - reporting type |
| Regulatory Reporting Country | Regulatory reporting information - reporting country |
| Regulatory Reporting Date | Regulatory reporting information - reporting date |
| Regulatory Reporting Code | Regulatory reporting information - reporting code |
| Regulatory Reporting Amount | Regulatory reporting information - reporting amount |
| Regulatory Reporting Currency | Regulatory reporting information - currency |
| Regulatory Reporting Information | Regulatory reporting information - line 1 |
| Remittance Identification | Related remittance information identification |
| Remittance Location Method | Related remittance information location method |
| Remittance Location Electronic Address | Related remittance information location e-address |
| Remittance Location Name | Related remittance location name |
| Remittance Location Town Name | Related remittance information town name |
| Remittance Location Country | Related remittance information location country |
| Remittance Location Address Line 1 | Related remittance information address line 1 |
| Creditor Reference Info Type Code | Creditor reference information type code in structured remittance information |
| Creditor Reference Info Type Issuer | Creditor reference information type issuer in structured remittance information |
| Creditor Reference Info Reference | Creditor reference information reference in structured remittance information |
| Instruction Priority | Instruction priority |
| Debtor Agent BIC | Debtor agent's BIC |
| Debtor Agent Clearing System ID | Debtor agent's clearing system identification |
| Debtor Agent Clearing Code | Debtor agent's clearing code |
| Debtor Agent Name | Debtor agent's name |

The product releases the keywords and any additions to the keywords must be brought to the notice of the product team, so that the same can be made available in the following AMR based on merits.

The product also provides a generic framework for defining the rules. Respective banks must create country-specific rules including the display of fixed value as drop-down list based on their requirements.

## Validating Payment

Temenos Transact modules such as Payment Order and Temenos Payment Hub can request this table with the required input parameters by invoking the public routine (API).

When a request is received through an embedded call, the system selects the most appropriate rules table and validates against the data received as input parameters.

Payments are validated against the various rules in the following sequence:

- If the destination country belongs to a country group, then the payment is validated against the country group rules.
- If the rule is defined for a destination country, then the payment is validated against that country rules.
- If the payment currency's country and destination country are different, then the payment is validated against the payment currency rules.

A payment can be subjected to validation of all the three rules, or any two, or only one depending on the payment data.

When the validation is successful for all the rules defined in the appropriate table, an ‘OK’ response is returned to the call.

In case of validation failures, ‘NOK’ along with the error or override texts are returned as a response to the call. If there are multiple validation failures, then all the errors are returned.

If the rules are not defined for a country, then payment processing is continued.

In this topic

- [Introduction to Country Validation](#IntroductiontoCountryValidation)

- [Defining Field Validation](#DefiningFieldValidation)
- [Setting up Rule](#SettingupRule)
- [Pre-defined Keywords](#PredefinedKeywords)
- [Validating Payment](#ValidatingPayment)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:24:48 PM IST