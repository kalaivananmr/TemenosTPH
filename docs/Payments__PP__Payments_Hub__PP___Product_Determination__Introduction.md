# Introduction to Product Determination

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Product_Determination/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Temenos Payments Hub > Product Determination > Introduction

- Temenos Payments Hub;)
  - [Introduction](../../Payments_Hub_(PP)/Misc/Introduction.htm)
  - [Messaging Framework Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Introduction.htm)
  - Clearing;)
  - Sanction Screening;)
  - Status Reporting;)
  - Cheque Clearing;)
  - Code Words;)
  - Direct Debits;)
  - International Payments (MT);)
  - Manual Repair;)
  - Business Dates;)
  - Posting;)
  - Fees and Billing;)
  - Funds Reservation;)
  - Warehousing;)
  - Book Transfer;)
  - Investigations and Enquiries;)
  - Routing and Settlement;)
  - Business Validations;)
  - Static Data;)
  - Standalone Payments;)
  - [Standalone Implementation Options Standalone Implementation Options](../../Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm)
  - Forex;)
  - Bulk Payments;)
  - Bank Condition;)
  - Client Condition;)
  - Product Determination;)
    - [Introduction](../../Payments_Hub_(PP)/Product_Determination/Introduction.htm)
    - [Configuration](../../Payments_Hub_(PP)/Product_Determination/Configuration.htm)
    - [Working with](../../Payments_Hub_(PP)/Product_Determination/Working_with.htm)
    - [Tasks](../../Payments_Hub_(PP)/Product_Determination/Tasks.htm)
    - [Outputs](../../Payments_Hub_(PP)/Product_Determination/Outputs.htm)
  - Housekeeping Functions;)
  - FATF and WTR2;)
  - PSD2;)
  - SWIFT gpi;)
  - SWIFT Universal Confirmations;)
  - Instant Payments;)
  - Agency Banking;)
  - Returns and Reversal;)
  - Exceptions and Investigations;)
  - Clearing Status Report;)
  - Monitoring;)
  - Counterparty Risk;)

Payments

# Introduction to Product Determination

Updated On 22 March 2025 |
 18 Min(s) read

Feedback
Summarize

Bank offers payment products for a wide variety of clients to suit their business needs. The commercial payment products of the bank are differentiated based on the following:

- Geography (domestic, SEPA, cross border)
- Payment Type (credit transfer, direct debits, cheques, etc.)
- Currency and Amount Value (high or low value)
- Volume (batch single)
- Priority (urgent or normal)
- Charges for processing payments

Bank needs to comply with regulatory requirements in EU or EEA, such as Payment Services Directive (PSD), which regulates the floats and fees on payments.

Product Determination (PD) component performs the following:

- Builds payment processing products within the STP engine, which caters to the business needs of the banks.
- Drives efficient processing within the payment engine.

Each product consists of a set of system defined input attributes and output parameters. The main feature of PD is to calculate the payment product by comparing the payment attributes and retrieving the output parameters for further processing. These output parameters become input to subsequent processing components, such as Posting, R&S, Fees, etc.

The STP engine receives a number of payments throughout the day and processes them quickly and efficiently. Hence, after accepting and before processing the payment message, it checks the payment characteristics. Temenos Payments Hub assigns weight to different types of payment messages to influence the processing of the payment message. The weight assigned depends on the complexity and combinations of the payment attributes.

[Example](#)

If the payment attributes are more complex with many combinations, then higher weight is assigned to it. The following are the classifications in payment messages:

| Classification | Description |
| --- | --- |
| Heavy | SWIFT based cross border payments and book transfers.  - International payments – Cross border payments sent and received using SWIFT. - Domestic payments – Payments in local currency originating and ending within the same country. |
| Medium | Payments initiated for clearing systems (credit transfer, direct debit), such as SEPA or USACH. |
| Light | All other payments from and to clearing systems and indirect participants. For example, incoming SEPA payments. |

## Product Flavours

Temenos Payments Hub provides different product flavours for payment processing (based on the weight) to enable attribute based product definition and efficient processing. According to the payment characteristics, each product flavour is defined using a set of system defined attributes. Temenos Payments Hub can configure multiple products of any flavour for efficient processing. The following are the product flavours:

| Product Flavours | Description |
| --- | --- |
| Heavy weight product | Processes heavy weight payment messages. For example, international SWIFT payments and book transfers. |
| Medium weight product | Processes medium weight payment messages. For example, outward credit transfer payments to SEPA. |
| Light weight product | Processes light weight payment messages. For example, incoming message from SEPA. |

A set of system defined output attributes (configurable by users) is available for each product. These output attributes (also known as output parameters) drive the processing of the payment by the following subsequent STP components:

- Client condition
- Routing and settlement
- Date determination
- Filtering
- Fees and posting scheme

## Input Attributes

Payments are classified as heavy, medium or light based on the characteristics. Temenos Payments Hub defines a set of input attributes (also known as product conditions) for each of these product flavours. The bank users can create multiple products of any flavor using different combination of input attributes for efficient processing. The following are the input attributes:

| Attribute | Description |
| --- | --- |
| *CTRBTR Indicator* | Identifies whether the payment is a customer payment or bank transfer. This enables to configure separate products to process customer payments or bank transfers. |
| *Payment Direction* | Identifies direction of the payment:  - Incoming - Outgoing - Book - Redirect   This enables to configure separate products to process incoming and outgoing payments. |
| *Domestic International* | Identifies whether the payment is domestic or international. This enables to configure separate products to process international payments and domestic payments. |
| *Single Batch Clearing* | Identifies whether the payment processed is single or batch payment. This enables to configures separate products for batch payments. |

To know more about the list of input attributes, refer to [Configuring Product Determination](Configuration.htm) section.

## Output Attributes

A set of output attributes is defined in the system for each of the product flavours. These output parameters become input for the subsequent components of the payment engine to process the payment. The following are the output attributes:

| Attribute | Description |
| --- | --- |
| *Client Condition Product* | Input for client condition component. |
| *Routing Product Group* | Input for routing and settlement component. |
| *Fee Product Group* | Input parameter for fees component. |
| *Posting Product Group* | Input parameter for posting component. |
| *Dates Product Group* | Input parameter for date component |

This is used for processing the payment.

To know more about the full list of output attributes, refer to [Configuring Product Determination](Configuration.htm) section.

## Determining Product

The main feature of PD component is to calculate the payment product and retrieve the output parameters. The products have a set of system defined input attributes, which are based on the characteristics of the payment. The weight to be assigned depends on the complexity and combinations of the payment attributes. Therefore, heavy weight payment has more attributes compared to medium and light weight product flavours.

When Temenos Payments Hub receives an incoming or outgoing payment, it assigns weight. PD component then compares the payment details against the products defined in the system for that flavour based on the weight. The banks define multiple products for each flavour to process it (based on different condition) using the attributes. Temenos Payments Hub uses Peeling Off mechanism to identify the right product for processing.

[Heavy Weight Peeling Off](#)

The heavy weight product condition consists of a large number of input attributes, which are used to define multiple products. Incoming payments data is matched against the input attributes to find the best match by using Peeling Off mechanism. To perform efficient matching, the input attributes are categorised into the following groups:

- Level 1
- Level 2
- Level 3

The *Fromamount* and *Toamount* fields are not part of these groups.

| Level 1 Attributes | Level 2 Attributes | Level 3 Attributes |
| --- | --- | --- |
| *Company ID* | *Ordering Institution BIC Present* | *Debit Account Type* |
| *CTRBTRIndicator* | *Beneficiary BIC Present* | *Sender BIC* |
| *Payment Direction* | *OrderingParty IBAN Present* | *Receiver BIC* |
| *Domestic International* | *Chargable Change* | *Incoming Message Type* |
| *Message Priority* | *Final Code Word* | *Validation Flag* |
| *Single Batch Clearing* | *Code Word Text* |  |
| *Originating Source* | *Intra Company Payment* |  |
| *Return Trigger* \ *Incoming Message Type* | *Banking Priority* |  |
| *Currency* | *Originating DebitParty Country* |  |
| *Charge Type* | *OrderingParty IBAN Country* |  |
|  | *Sender Country* |  |
|  | *OrderingParty Residency* |  |
|  | *Beneficiary Country* |  |
|  | *BeneficiaryParty IBAN Country* |  |
|  | *Receiver Country* |  |

[Level 1 Peeling Off](#)

A heavy weight payment is matched against heavy weight products by using one of the following steps:

- Ensure that every payment passes one of the following steps: 1, 2, 3 or 4.
- If a matching product is not found, it moves the payment to Manual Repair and displays an error.

| Step | Description |
| --- | --- |
| Step 1 – Check the record with specific currency along with level 1 attributes. | - If a record with specific currency is found in level 1, check for a matching record across all the fields in level 1. - If a matching record is found, check for matching record in level 2 and 3. - If a match is not found in level 2 and 3 after respective peeling offs, set the *Charge Type* to ‘\*’ in level 1. - If a record is found in level 1 with *Charge Type* peeled off, set ‘\*’ in all fields of level 2 and 3 to match the records. - If a matching record is not found with ‘\*’ fields in level 2 and level 3, set the *Currency* field as ‘\*’ in level 1 and ‘\*’ in level 2 and 3 fields to find a match. - If a matching record is not found, the level 1 peeling off and subsequent matching process continue till *Originating Source* field. |
| Step 2 – If a record with currency along with specific field is not found in level 1, check a record with specific currency, other Level 1 fields, and *Charge Type* set to ‘\*’. | - If a matching record is not found in level 1, the system checks according to Step 3. - If a record is found in level 1, then all level 2 and 3 fields are set as ‘\*’ to find a match. - If a matching record is not found with ‘\*’ fields in level 2 and 3, the *Currency* field is set to ‘\*’ in level 1. All level 2 and 3 all fields are then matched with ‘\*’. - If a matching record is not found, then level 1 peeling off and subsequent matching process continue till *Originating Source* field. |
| Step 3 – If level 1 record is not found using Step 1 and 2, check whether records are found using currency group to which the currency belongs. | The process mentioned in Step 1 or 2 is performed to find a matching product. |
| Step 4 – If a record is not found in step 1, 2 or 3, check a record with *Currency* as ‘\*’, specific level 1 fields, and *Charge Type* set to ‘\*’. | - If a matching record is found in level 1, check for matching level 2 and 3 records with all fields set as ‘\*’ (since level 1 is peeled off, all subsequent fields in right needs to be peeled off). - If matching record is not found in level 1, set the *Originating Source* and *Return Trigger* fields as ‘\*’ to check for the matching record. |

[Level 2 Peeling Off](#)

If a specific record is found in level 1 without peeling off, check in level 2.

- If a match is found in level 2, then level 3 is matched using level 3 peeling off.
  - If a matching record cannot be found in level 3, matching process goes back to level 2 with normal peeling off ( changed to \*) from right to left till a record is found in level 2.
  - Once fields are peeled off in level 2 using ‘\*’, set ‘\*’ in all fields of level 3 to find a match.
  - If a matching record is not found after peeling off in level 2 and 3, matching process goes back to level 1 to try next level peeling off.
- If match is not found in level 2, the following occurs:
  - The country code in *Receiver Country* field is changed to corresponding country group and level 2 fields are not changed.
  - If a matching record is still not found using the country group or the *Receiver Country* field does not belong to a country group, the *Receiver Country* field is changed to ‘\*’.
  - If a matching level 2 record is found with peeled off *Receiver Country*, then all level 3 fields are matched for ‘\*’.
  - If a record does not exist in level 2 after peeling off ‘\*’ value in *Receiver Country*, the above steps (which were performed for *Receiver Country*) are performed for the next country *BeneficiaryParty IBAN Country* field with various combinations of *Receiver Country* field ( country code>country group>‘\*’). The rest of the fields in level 2 are retained. These steps are repeated until a matching record is found (till the left most country *Originating DebitParty Country* field).

The following list of level 2 country related fields are checked using the above mentioned process from right to left (*Receiver Country* till *Originating DebitParty Country*):

- *Originating DebitParty Country*
- *OrderingParty IBAN Country*
- *Sender Country*
- *OrderingParty Residency*
- *Beneficiary Country*
- *BeneficiaryParty IBAN Country*
- *Receiver Country*

[Level 3 Peeling Off](#)

- If a specific record is found in level 1 and level 2, then a record is checked in level 3.
- If a match is not found, then matching process uses peeling off (changed to ‘\*’) from right to left) for level 3.
- If a record is not found after the peeling off in level 3, the following occurs:

  |  |  |
  | --- | --- |
  | Matching process goes back to level 2 to try next level of peeling off for the already matched level 1 record. | - If a record is found after applying the peeling off ( change to \*) to the last Receiving Country field in level 2, then a record is checked again in level 3 with all fields peeled off to \*. - If a record is not found, the level 2 peeling off continues to find a matched level 2 and 3 record. |
- If a record is not found by following the above repeated steps in level 2, the matching process goes back to level 1 peeling off ( mentioned in section ‘Level 1 peeling off ‘ ). Once the field is peeled off (\*) in level 1, then all fields in level 2 and 3 are matched for ‘\*’.

[Medium Weight Peeling Off](#)

The Peeling Off mechanism used for medium weight products is same as heavy weight products. The medium weight input attributes are categorised into the following groups:

- Level 1
- Level 2
- Level 3

The *Fromamount* and *Toamount* fields are not part of these groups.

If a matching product is not found, it moves the payment to Manual Repair and displays an error.

| Level 1 Attributes | Level 2 Attributes | Level 3 Attributes |
| --- | --- | --- |
| *Company ID* | *Source Group* | *Ben Pty IBAN Present* |
| *Payment Direction* | *Message Type* | *Ord Pty IBAN Present* |
| *Clearing Transaction Type* | *Clearing Nature Code* | *Ben BIC Present* |
| *Single Batch Clearing* | *Ben Pty IBAN Ctry* | *Ord BIC Present* |
| *Charge Type* | *Ord Pty IBAN Ctry* | *Ord Pty Residency* |
| *Currency* |  | *Final Codeword* |

[Light Weight Peeling Off](#)

Light weight payments are matched with product conditions by using simple right to left Peeling Off mechanism. A specific match is checked with all field values of light weight product.

- If a match is not found, the right most field is set to ‘\*’ (peeled off) and match record is checked.
- If a match is not found, then the second last field from right is set to ‘\*’ (peeled off) and match record is checked.

This process of peeling off continues from right to left to find a matching product.

If a matching product is not found, it moves the payment to Manual Repair and displays an error.

## Account Switching

The system automatically redirects a payment when the beneficiary account is switched to another bank. It is applicable for inward and book payments, when Temenos Payments Hub is implemented in embedded mode with Temenos Transact. During payment processing, Temenos Payments Hub validates whether the beneficiary account is switched out. If yes, the following takes place in Temenos Payments Hub:

- Receives the switch out details (such as new account number, BIC or Clearing Code of new bank, which are maintained in Temenos Transact level)
- Except the payments received from the new bank account, the system redirects all the payments to the new bank account. If the payment is received from the account of the new bank, the system parks the payment in the repair queue.

This feature is applicable for all clearing transaction types except DD (Direct Debits) payments.




- This function is available only with PH license.
- It is dependent on the BFW module (License: ACSWIT) in Temenos Transact to capture account switching details.

## Product Output Refinement

After determining a payment product, it is possible to refine the product output further based on the conditions defined in the refinement. The user can define the conditions based on the payment parameters in the Refinement table. When the conditions for refinement is satisfied, the refinement applies over the top of the output attributes already determined in the product determination. Although the output attributes are refined, it is still possible for the output attribute to be modified in later stages of STP and the more recent updates are considered for the payment processing. The same output attributes can be refined at different stages and the more recent update takes precedence.

The refinement impacts the following components in the STP flow:

- Product Determination
- Debit Client Condition
- Routing product
- Credit Client Condition
- Filtering product
- Fee Product

Refinement in product determination activation phase works after the product is determined. For other activation phase mentioned in the list, they are dependent on the output of the Product Determination module. For example, the selection of debit client condition refinement is based on the Client Condition Product output parameter defined in the Product Determination table. The derived output can have a refinement defined for the respective activation phase.

The refinements are activated before the actual component processing starts. The only exception is the product determination component where the refinement occurs after the product is determined. Both the condition defined and the output to be refined are dependent on what phase it is getting processed. If the component is skipped, then the product refinement is also skipped along with the component.

In this topic

- [Introduction to Product Determination](#IntroductiontoProductDetermination)

- [Product Flavours](#ProductFlavours)
- [Input Attributes](#InputAttributes)
- [Output Attributes](#OutputAttributes)
- [Determining Product](#DeterminingProduct)
- [Account Switching](#AccountSwitching)
- [Product Output Refinement](#ProductOutputRefinement)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:55:30 PM IST