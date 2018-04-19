# Stubs for prov.model (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from prov.constants import *
from prov import Error
from typing import Any, Optional

__email__: str
logger: Any

def parse_xsd_datetime(value): ...
def parse_boolean(value): ...

DATATYPE_PARSERS: Any
XSD_DATATYPE_PARSERS: Any

def parse_xsd_types(value, datatype): ...
def first(a_set): ...
def encoding_provn_value(value): ...

class Literal:
    def __init__(self, value, datatype: Optional[Any] = ..., langtag: Optional[Any] = ...) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    @property
    def value(self): ...
    @property
    def datatype(self): ...
    @property
    def langtag(self): ...
    def has_no_langtag(self): ...
    def provn_representation(self): ...

class ProvException(Error): ...
class ProvWarning(Warning): ...

class ProvExceptionInvalidQualifiedName(ProvException):
    qname: Any = ...
    def __init__(self, qname) -> None: ...

class ProvElementIdentifierRequired(ProvException): ...

class ProvRecord:
    FORMAL_ATTRIBUTES: Any = ...
    def __init__(self, bundle, identifier, attributes: Optional[Any] = ...) -> None: ...
    def __hash__(self): ...
    def copy(self): ...
    def get_type(self): ...
    def get_asserted_types(self): ...
    def add_asserted_type(self, type_identifier): ...
    def get_attribute(self, attr_name): ...
    @property
    def identifier(self): ...
    @property
    def attributes(self): ...
    @property
    def args(self): ...
    @property
    def formal_attributes(self): ...
    @property
    def extra_attributes(self): ...
    @property
    def bundle(self): ...
    @property
    def label(self): ...
    @property
    def value(self): ...
    def add_attributes(self, attributes): ...
    def __eq__(self, other): ...
    def get_provn(self): ...
    def is_element(self): ...
    def is_relation(self): ...

class ProvElement(ProvRecord):
    def __init__(self, bundle, identifier, attributes: Optional[Any] = ...) -> None: ...
    def is_element(self): ...

class ProvRelation(ProvRecord):
    def is_relation(self): ...

class ProvEntity(ProvElement):
    def wasGeneratedBy(self, activity, time: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasInvalidatedBy(self, activity, time: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasDerivedFrom(self, usedEntity, activity: Optional[Any] = ..., generation: Optional[Any] = ..., usage: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasAttributedTo(self, agent, attributes: Optional[Any] = ...): ...
    def alternateOf(self, alternate2): ...
    def specializationOf(self, generalEntity): ...
    def hadMember(self, entity): ...

class ProvActivity(ProvElement):
    FORMAL_ATTRIBUTES: Any = ...
    def set_time(self, startTime: Optional[Any] = ..., endTime: Optional[Any] = ...): ...
    def get_startTime(self): ...
    def get_endTime(self): ...
    def used(self, entity, time: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasInformedBy(self, informant, attributes: Optional[Any] = ...): ...
    def wasStartedBy(self, trigger, starter: Optional[Any] = ..., time: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasEndedBy(self, trigger, ender: Optional[Any] = ..., time: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def wasAssociatedWith(self, agent, plan: Optional[Any] = ..., attributes: Optional[Any] = ...): ...

class ProvGeneration(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvUsage(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvCommunication(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvStart(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvEnd(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvInvalidation(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvDerivation(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvAgent(ProvElement):
    def actedOnBehalfOf(self, responsible, activity: Optional[Any] = ..., attributes: Optional[Any] = ...): ...

class ProvAttribution(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvAssociation(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvDelegation(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvInfluence(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvSpecialization(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvAlternate(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

class ProvMention(ProvSpecialization):
    FORMAL_ATTRIBUTES: Any = ...

class ProvMembership(ProvRelation):
    FORMAL_ATTRIBUTES: Any = ...

PROV_REC_CLS: Any
DEFAULT_NAMESPACES: Any

class NamespaceManager(dict):
    parent: Any = ...
    def __init__(self, namespaces: Optional[Any] = ..., default: Optional[Any] = ..., parent: Optional[Any] = ...) -> None: ...
    def get_namespace(self, uri): ...
    def get_registered_namespaces(self): ...
    def set_default_namespace(self, uri): ...
    def get_default_namespace(self): ...
    def add_namespace(self, namespace): ...
    def add_namespaces(self, namespaces): ...
    def valid_qualified_name(self, qname): ...
    def get_anonymous_identifier(self, local_prefix: str = ...): ...

class ProvBundle:
    def __init__(self, records: Optional[Any] = ..., identifier: Optional[Any] = ..., namespaces: Optional[Any] = ..., document: Optional[Any] = ...) -> None: ...
    @property
    def namespaces(self): ...
    @property
    def default_ns_uri(self): ...
    @property
    def document(self): ...
    @property
    def identifier(self): ...
    @property
    def records(self): ...
    def set_default_namespace(self, uri): ...
    def get_default_namespace(self): ...
    def add_namespace(self, namespace_or_prefix, uri: Optional[Any] = ...): ...
    def get_registered_namespaces(self): ...
    def valid_qualified_name(self, identifier): ...
    def get_records(self, class_or_type_or_tuple: Optional[Any] = ...): ...
    def get_record(self, identifier): ...
    def is_document(self): ...
    def is_bundle(self): ...
    def has_bundles(self): ...
    @property
    def bundles(self): ...
    def get_provn(self, _indent_level: int = ...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Any = ...
    def unified(self): ...
    def update(self, other): ...
    def new_record(self, record_type, identifier, attributes: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def add_record(self, record): ...
    def entity(self, identifier, other_attributes: Optional[Any] = ...): ...
    def activity(self, identifier, startTime: Optional[Any] = ..., endTime: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def generation(self, entity, activity: Optional[Any] = ..., time: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def usage(self, activity, entity: Optional[Any] = ..., time: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def start(self, activity, trigger: Optional[Any] = ..., starter: Optional[Any] = ..., time: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def end(self, activity, trigger: Optional[Any] = ..., ender: Optional[Any] = ..., time: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def invalidation(self, entity, activity: Optional[Any] = ..., time: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def communication(self, informed, informant, identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def agent(self, identifier, other_attributes: Optional[Any] = ...): ...
    def attribution(self, entity, agent, identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def association(self, activity, agent: Optional[Any] = ..., plan: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def delegation(self, delegate, responsible, activity: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def influence(self, influencee, influencer, identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def derivation(self, generatedEntity, usedEntity, activity: Optional[Any] = ..., generation: Optional[Any] = ..., usage: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def revision(self, generatedEntity, usedEntity, activity: Optional[Any] = ..., generation: Optional[Any] = ..., usage: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def quotation(self, generatedEntity, usedEntity, activity: Optional[Any] = ..., generation: Optional[Any] = ..., usage: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def primary_source(self, generatedEntity, usedEntity, activity: Optional[Any] = ..., generation: Optional[Any] = ..., usage: Optional[Any] = ..., identifier: Optional[Any] = ..., other_attributes: Optional[Any] = ...): ...
    def specialization(self, specificEntity, generalEntity): ...
    def alternate(self, alternate1, alternate2): ...
    def mention(self, specificEntity, generalEntity, bundle): ...
    def collection(self, identifier, other_attributes: Optional[Any] = ...): ...
    def membership(self, collection, entity): ...
    def plot(self, filename: Optional[Any] = ..., show_nary: bool = ..., use_labels: bool = ..., show_element_attributes: bool = ..., show_relation_attributes: bool = ...): ...
    wasGeneratedBy: Any = ...
    used: Any = ...
    wasStartedBy: Any = ...
    wasEndedBy: Any = ...
    wasInvalidatedBy: Any = ...
    wasInformedBy: Any = ...
    wasAttributedTo: Any = ...
    wasAssociatedWith: Any = ...
    actedOnBehalfOf: Any = ...
    wasInfluencedBy: Any = ...
    wasDerivedFrom: Any = ...
    wasRevisionOf: Any = ...
    wasQuotedFrom: Any = ...
    hadPrimarySource: Any = ...
    alternateOf: Any = ...
    specializationOf: Any = ...
    mentionOf: Any = ...
    hadMember: Any = ...

class ProvDocument(ProvBundle):
    def __init__(self, records: Optional[Any] = ..., namespaces: Optional[Any] = ...) -> None: ...
    def __eq__(self, other): ...
    def is_document(self): ...
    def is_bundle(self): ...
    def has_bundles(self): ...
    @property
    def bundles(self): ...
    def flattened(self): ...
    def unified(self): ...
    def update(self, other): ...
    def add_bundle(self, bundle, identifier: Optional[Any] = ...): ...
    def bundle(self, identifier): ...
    def serialize(self, destination: Optional[Any] = ..., format: str = ..., **args): ...
    @staticmethod
    def deserialize(source: Optional[Any] = ..., content: Optional[Any] = ..., format: str = ..., **args): ...

def sorted_attributes(element, attributes): ...