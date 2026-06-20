# Introduction to Routing and Settlement - Top

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm#top

---

2. [Payments](../../../../content/payments.html)

- Europe;)

Payments

# Introduction to Routing and Settlement

Updated On 22 March 2025 |
 23 Min(s) read

Feedback
Summarize

The process of identifying the appropriate channel for sending the payment to its customer is termed as Routing and Settlement (R&S). The beneficiary can be present in the bank, when a user initiates a credit transfer. This payments is termed as Book Transfers and do not require R&S. If the beneficiary is not available with the processing bank, then R&S plays an important role:

- In outgoing and redirected payments, the beneficiary can be present with a correspondent bank or clearing in which both the processing and beneficiary banks are participants.
- Additionally, it determines the appropriate routing channel through which the beneficiary can be reached and routes the payment.

Similarly, for a direct debit, R&S plays a vital role in identifying the appropriate clearing for an outgoing or redirected direct debit payment.

## Inputs Required by R&S to Determine a Channel

To route a payment to a specific channel, R&S requires the following information:

|  |  |
| --- | --- |
| Transaction Amount | Each clearing has its own rules for accepting payments. Therefore, user needs to configure R&S to send payments to relevant clearing channels, based on denominations or values. |
| Transaction Currency | Clearing channels provide services only in certain currencies. Hence, user needs to configure each clearing channel to its appropriate currency. For example, STEP2 accepts only EURO currency. |
| Payment Priority | User can configure the appropriate payment channel based on the payment priority.  For example, high priority payments are routed through CHAPS and low priority payments through BACS. |
| Charging Option | Companies have flexibility in defining the routing based on the charging option.  For example, a company can route an OUR payment through a certain correspondent, and SHA or BEN payment through another correspondent. |
| Payment Characteristics | Each payment has its own characteristics, based on which payment is routed to the appropriate clearing. There are various parameters based on which, payments can have different routing options. To know how different rules are applied on payment processing, refer to [Product Determination](../Product_Determination/Introduction.htm). For example, domestic and international payments can be routed to different clearings. User needs to configure appropriate routing channel in the product table for the given characteristic of the payment. This routing channel is termed as Routing Product in Temenos Payments Hub. |
| Business Line | Banks categorises its customers based on their profile. For example, customers fall into various categories, such as high net worth individuals, corporates, blue chip companies, etc. Additionally, it provides the flexibility to route payments to different channels based on customer profile. |

System-specific product are prefixed with ‘CORE’ for special processing based on conditions defined by product. For example, ‘CORE\_IMPCO’ is a system-specific product to pass the configured cut-off time for all incoming and book payments. Other routing products pass the cut-off time as Close of Business (COB) for all incoming and book payments.

## Routing Methods

The following are the supported routing methods:

| Routing Method | Description |
| --- | --- |
| Preferred Correspondent (Country Correspondent) - PREF | Preferred Correspondent is a correspondent bank of choice for payment to a particular country. Routing and Settlement (RS) has an ability to store a “Preferred Correspondent” per country (also known as country correspondent). For example, if a payment needs to be routed to Germany and the R and S rules are set in such a way that the credit bank can be reached through its country correspondent, then the RS module should determine the country correspondent for Germany and route the payment through that bank. |
| Currency Correspondent - SSI | Based on the currency of the payment, the creditor bank can have a currency correspondent. Currency correspondents are released by SWIFT as part of Standing Settlement Instructions file. For example, if a payment in USD needs to be routed to Deutsche Bank in Germany and the RS rules are set in such a way that the creditor bank can be reached through its currency correspondent, then the RS module should determine the currency correspondent for Deutsche Bank and route the payment through the bank.  - The system looks up currency correspondent based on currency and routing product (*Asset Category* and other fields do not influence the selection of correspondent). - TPH does not support SWIFT Ref API to retrieve the SSI’s record for BIC. |
| Head Office - Branch relationship -AGENT | RS has an ability to store a head office - branch relationship (on BIC code level) within the Payment engine. The AGENT table holds head office - branch relationships between institutions. For example, DEUTDEFF can be defined as the head office for DEUTDEFF500. If a payment is to be routed to DEUTDEFF500 and the RS rules are set in such a way that the creditor bank can be reached through its head office then RS should route the payment through DEUTDEFF. |
| PARTY | Creditor bank can be reached by the financial institution mentioned in the contract agreement. Payment is routed through the financial institution if the processing bank has the LORO or NOSTRO relationship with it. This bank is the new creditor bank for the payment chain. |
| LORO or NOSTRO | Payment can be routed to the credit party by using their LORO or NOSTRO accounts. The payment is routed and settled with the help of a LORO or NOSTRO account that is shared with the creditor bank. |
| ACCOUNT | An account can be defined through which the settlement can be carried out. This account can be different from the LORO or NOSTRO account of the creditor bank. RS option of ACCOUNT is similar to the LORO or NOSTRO RS option. The only difference being that the account used to settle is provided in the RS option itself. The account could be a LORO account, NOSTRO account, or an internal account or suspense account. |
| CLEARING CHANNEL / RTGS SYSTEM | A payment can be routed to the credit party using a clearing channel or RTGS system. For example, EMZ clearing can be used to route a EUR payment in Germany. Every clearing channel or RTGS system has a set of rules for the payments that it can process. For example, TARGET2 can only process payments in EUR currency. The payment should therefore clear these channel level validations for it to successfully select the Clearing channel or RTGS RS option. |

## Determining a Channel

R&S determines a suitable routing channel for the payment based on the following:

1. **Pre-Configured Routing Rules**

   User configures the routing channels according to the input parameters. For example, if the user needs to route a payment to STEP2 clearing, then define it for EURO currency. Similarly, for other criteria (as mentioned in above section) suitable channels are defined. R&S has the following rules to select a channel:

   - If the intended end customer can be reached directly by a correspondent bank, then priority is given to the channel.
   - If correspondent relationship is not available with any bank, it is validated by the destination country (that is, whether the bank has a relationship within the destination country of the end customer).
   - If the destination country cannot be derived, the company’s home country is considered as the destination country to find a channel.
   - If country level relationship is not available, it selects the least specific bank level routing channel.

   Additionally, R&S provides the flexibility to define currency correspondents (that is, payments can be routed to pre-defined correspondent for a given currency). If the payment can be reached only through clearing channel, a corresponding clearing channel needs to be selected.
2. **Channel Validations**

   R&S performs certain validations on payments. If any of the validations fail, then it:

   - Searches for the next suitable channel or destination country
   - Places the payment in Repair queue based on configurations.

   To know more, refer to [Performing Channel Validation](#Performing_Channel_Validation) section.
3. **Requested Credit Value Date (RCVD) in the Payment**

   After identifying the channel, R&S performs one of the following:

   - Investigates whether the payment can be forwarded to the channel within the cut-off time of CVD.
   - Processes the payment immediately by bumping the CVD (based on shifts) or warehouses the payment till the CVD are met (based on shifts).

   - This setup can be configured in the system.
   - Dynamic routing to the next available channel is offered with the PH License.
   - If IBAN is present as the payment’s top credit party, TPH derives the BIC from that IBAN using RD.CENTRAL.BANK.DIR. This derivation happens irrespective of the NoBicBkCdValidation configuration in PP.COMPANY.PROPERTIES or PP.CLEARING.

## Performing Channel Validation

R&S can perform validations on any selected channels. If the validation fails, it can be configured to select the next channel or send the payment to repair.

| Channel Level Validations | |
| --- | --- |
| Different Types of Authentication | Detail |
| Reachability Check | Verifies whether the credit bank is reachable in the respective Clearing Directory. The Clearing Directory records are stored in the CA.CLEARING.DIRECTORY table.  - To search, go to **Admin Menu**>**Framework parameter**>**Clearing Directory**>**Search Clearing Directory**.  In some clearings, reachability check is performed:  - To confirm whether it is a valid National Clearing Code (NCC). For example, any bank in UK that has a valid sort code is reachable by the BACS clearing. - To determine direct participant for a clearing. This differs from clearing to clearing.   If reachability check fails, then routing cannot be performed with that clearing channel or RTGS system. R&S needs to check the following for Loro or Nostro:  - Valid credit BIC - Have a Loro or Nostro account with the company. If available, the credit BIC is reachable by Loro or Nostro. |
| Relationship Management Application (RMA) Check | Bank can control the institutions that can send SWIFT messages to banks. The objective is to stop unwanted messages from the sender. The bank can decide the following with RMA:  - Banks that can send messages to them - Message types that the bank can send - Dates within which the messages can be sent (in some cases) |
| Cut-Off Time Check | Every clearing or RTGS system has a certain cut-off time, which is used to determine the following:  - Decides whether to accept a payment or not for certain clearing channels or RTGS systems. For example, TARGET2 does not accept a payment after the cut-off time. - Value date applicable on the payment. For example, SEPA has two cycles. Any payment processed after the second cut-off time of the second cycle is processed with a value date of today + 1.   Using R&S, cut-off time can be determined based on *Channel, Currency (Transaction Currency), Direction, Priority, Message Type* and *Originating Source*. |
| Format Validations | A clearing channel, RTGS system or SWIFT can accept messages that comply to certain pre-defined rules (format validations). R&S checks whether the outgoing or redirected payment meets these format validation rules. If the format validations are successfully cleared, the routing channel is finalised.  If Nobicbkcdvalidation in PP.CLEARING or PP.COMPANY.PROPERTIES is set as Y, then validating the payments BIC against RD.CENTRAL.BANK.DIR is skipped as part of common validations. |

- When NCC is provided as the top credit party and NoBicBkCdValidation is set as Y at PP.COMPANY.PROPERTIES or PP.CLEARING, the BIC is not validated against RD.CENTRAL.BANK.DIRECTORY
- When BIC and NCC is provided as the top credit party and NoBicBkCdValidation is set as Y at PP.COMPANY.PROPERTIES or PP.CLEARING, TPH does not validate if the BIC and NCC belong to the same entity.

## Performing Country Rules Check

R&S can perform validations based on the destination country. If the validation fails, based on the source settings, the payment is either cancelled automatically or moved to the repair queue.

| Authentication | Detail |
| --- | --- |
| Country Rules Check | TPH sends the payment details to the Country Payment Conditions module to validate if the payment conforms the rules of the destination country. The country rules are defined in the CV.BEN.COUNTRY.CONDITIONS table. To view the country rules, go to **Admin Menu > Payments > Country Validation > Country Validation List**.  Based on the response, the payment processing is either continued or moved to Repair or Cancelled.  Country payment conditions check is done only when:   - The PSINCV license is installed - The payment is classified as ‘I’ (international)   and is an outgoing credit transfer |

## Importance of Dates in Channel Determination

R&S tries to meet RCVD, when it is specified in the payment. It checks the list of pre-defined routing channels (configured in respective R&S contract) to find a channel that can meet the RCVD. If the RCVD cannot be met, it performs the following:

- Payment is sent to repair or CVD
- Processing date is advanced based on the configuration in respective R&S contract

## Impact of Channel Determination in Identifying Credit Party

R&S contract is configured with multiple credit parties to be considered for routing the message. This list of credit parties is used by:

- Payment advising to create the SWIFT message.

  If a payment is routed through a preferred correspondent (Country Correspondent), then both the preferred (correspondent and beneficiary) banks need to be stored within R&S.
- Payment generation module to create the payment message.

R&S can handle a maximum of six credit parties on a payment. Whereas, payment can handle a maximum of three credit parties using serial method.

If it exceeds the limit, the payment is sent to repair.

## R&S for Payments Initiated from Order Entry

The processing within the R&S module is the same, even when the payment is initiated from other delivering channels. It applies the same rules or logic to determine the R&S channel and applicable credit party, irrespective of the delivering channel that initiates it. To initiate or resubmit the payment from Manual Entry and Repair pages, the user can impose the channel through which the payment needs to be routed. If imposed, then R&S:

- Logic does not go through the rules to determine the R&S channels and applicable credit party.
- Performs the R&S channel validation rules.

## R&S for Direct Debits

In the R&S channel selection table (PP.RSCHANNEL.SELECTION), the system:

- Captures the routing contracts for direct debits
- Searches for matching records for routing direct debit payment

In the same R&S contract, different output channels can be configured for different payment attributes (such as *Transaction Currency, Destination Country, Priority,* etc.). The system compares the payment attributes that are processed against the configured values in the record, and identifies the output channel that matches. If multiple output channels match the attributes of the payment, then the corresponding matching record with highest ranking is retrieved. Highest ranking is the record with the lowest rank value. The system then performs channel reachability and validation before routing the payment using the selected channel. If there are any functional errors while retrieving the output channel, the system routes the payment to Repair queue.

## Routing Payments through Serial and Cover Method

R&S can send payments through Serial and Cover method when SWIFT is used to route the payment (using MT103 or MT103+ message).

- If the beneficiary bank is a correspondent to the company, R&S can route the payment through a Loro or Nostro.
- If the beneficiary bank can be reached through clearing channels or RTGS system, R&S can route the payment through that clearing channel or RTGS system.

However, if the beneficiary bank is not reachable by a correspondent relationship or clearing channel, a new credit bank (country correspondent, currency correspondent, etc.) is inserted into the payment. This helps to route the payment to the beneficiary bank using serial or cover method.

The routing method selected depends on the rules setup.

[Routing of Payments between Banks that Share Loro or Nostro](#)



[Routing with Serial Method](#)



In this payment method, the payment message (MT103) is sent to a correspondent bank determined by R&S. Hence, this correspondent bank needs to send the payment message to the beneficiary bank.

[Cover Method of Routing](#)



In this payment method, the payment message (MT103) is sent directly to the beneficiary bank even when the company does not share an account relationship with it. A separate cover payment message is sent to clear and settle the payment at an interbank level. The cover message can be sent through SWIFT or RTGS systems (such as TARGET2). To route payment with Cover method, set the *Cover Indicator* field of the respective R&S contract for the SWIFT based channel associated with the payment as Y as shown below.












## Routing Payments using Head Office – Branch Relationship

Temenos Payments Hub can store a head office to branch relationship (on BIC code level). R&S rules are configured which enables the system to refer the relationships and then route the payment.

If the following are defined, R&S routes the payment through DEUTDEFF:

- DEUTDEFF is defined as the head office for DEUTDEFF500
- Temenos Payments Hub processes a payment that needs to be routed to DEUTDEFF500
- System identifies that the R&S rules are set and the credit bank (DEUTDEFF500) can be reached through its head office (DEUTDEFF)

To know more about sample configuration, refer to [Configuring Routing and Settlement](Configuring.htm).

## Tag 53B (External Account Number)

Banks can send the account number that is credited or debited in Tag 53B of the outgoing message. This is mainly sent when sender of the message holds multiple accounts with the receiver in the transaction currency.

Temenos Payments Hub supports the following functionalities for Tag53B:

- Determines the credit account from Loro or Nostro table. If there are multiple accounts in the transaction currency, it includes the preferred credit account in Tag53B.
- If the credit account is imposed by the operator and is also available in the Loro or Nostro table with multiple accounts in the same currency, the credit account is included in Tag 53B.
- If the credit account imposed is not available in Loro or Nostro table, an error is raised to the Operator to correct or define the account in Loro or Nostro table to proceed.
- Maps the following:
  - Actual account number to Tag 53B in Loro.
  - External account number with the receiver in Nostro.

    Temenos Payments Hub does not populate external account details defined in `PP.LORO.NOSTRO.ACCOUNT` in Settlement account tag of the outward payment sent to Clearing (including TGT2 Clearing) or Tag 53B of Clearing payments in SWIFT format as the system refers to `PP.LORO.NOSTRO.ACCOUNT` for corresponding banking payments. To store and map external account number, the user must define the account number in `PP.CLEARING`. Read [Configuring Clearing](../Clearing/Configuration.htm) for more information.
- Once the account number is defined, Temenos Payments Hub refers to `PP.CLEARING` to fetch external account number defined in payment currency, store the details in transaction information and send it in the outgoing message.

## Supporting Configuration of Message Interface

The widely used network for CBPR+ messages is SWIFT Interact, which is currently supported by Delivery Module out of the box. But the bank can decide to use different network such as Managed File Transfer (MFT). The technical header in the outward message varies for each interface. Hence, TPH can configure the network to route CBPR+ messages at individual correspondent bank level (BIC or Account). When the payment is to be routed through the correspondent banks in CBPR+ format, the system refers to the configuration and stores this information in the transaction, which would be later passed to the DE layer. The DE layer is responsible for creating technical header based on the network. Refer to the [Configuring Routing and Settlement](Configuring.htm) topic for more information. Similarly, the system allows to configure the network for payment messages sent to clearing. When the payment is to be routed to clearing, the system refers to the network configuration at the corresponding clearing and this information is emitted from Temenos Payments Hub during message generation.

## Defining Nostro Quotas

Temenos Payments Hub receives, sends, and redirects payments. When the payment is sent, the receiver is identified based on the routing rules configured in the system. The bank can have multiple Nostro correspondents per currency (Credit main account Currency). The ability of the system to choose a Nostro correspondent based on the pre-defined criteria is referred as Nostro Quotas.

When the R & S option is determined to be ‘PREF’ based on routing rules, the system chooses the Nostro correspondent based on the pre-defined criteria.

## Routing and Settlement for camt.107

For issuance of FCY draft, the bank (drawer) must have a direct correspondent banking relationship with the drawee agent, including a Nostro account, and ChequePresentmentNotification (camt.107) is sent to the drawee bank.

Hence a company-level contract with NOSTRO as the only R&S option is required for routing the camt.107 message and it is also advisable to set alt for cut-off and alt for RS as ‘R’, which routes the payment to the repair queue in case of a cut-off miss or if the drawer bank does not hold Nostro accounting relationship with the drawee bank.

In this topic

- [Introduction to Routing and Settlement](#IntroductiontoRoutingandSettlement)

- [Inputs Required by R&S to Determine a Channel](#InputsRequiredbyRStoDetermineaChannel)
- [Routing Methods](#RoutingMethods)
- [Determining a Channel](#DeterminingaChannel)
- [Performing Channel Validation](#PerformingChannelValidation)
- [Performing Country Rules Check](#PerformingCountryRulesCheck)
- [Importance of Dates in Channel Determination](#ImportanceofDatesinChannelDetermination)
- [Impact of Channel Determination in Identifying Credit Party](#ImpactofChannelDeterminationinIdentifyingCreditParty)
- [R&S for Payments Initiated from Order Entry](#RSforPaymentsInitiatedfromOrderEntry)
- [R&S for Direct Debits](#RSforDirectDebits)
- [Routing Payments through Serial and Cover Method](#RoutingPaymentsthroughSerialandCoverMethod)
- [Routing Payments using Head Office – Branch Relationship](#RoutingPaymentsusingHeadOfficeBranchRelationship)
- [Tag 53B (External Account Number)](#Tag53BExternalAccountNumber)
- [Supporting Configuration of Message Interface](#SupportingConfigurationofMessageInterface)
- [Defining Nostro Quotas](#DefiningNostroQuotas)
- [Routing and Settlement for camt.107](#RoutingandSettlementforcamt107)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:22:29 PM IST