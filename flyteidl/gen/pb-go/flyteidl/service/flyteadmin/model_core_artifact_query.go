/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type CoreArtifactQuery struct {
	ArtifactId *CoreArtifactId `json:"artifact_id,omitempty"`
	ArtifactTag *CoreArtifactTag `json:"artifact_tag,omitempty"`
	Uri string `json:"uri,omitempty"`
	// This is used in the trigger case, where a user specifies a value for an input that is one of the triggering artifacts, or a partition value derived from a triggering artifact.
	Binding *CoreArtifactBindingData `json:"binding,omitempty"`
}